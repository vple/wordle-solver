import string
import itertools
from filters import *
from collections import Counter
from copy import deepcopy
import typing

from wordle_types.state import *
from wordle_types.candidate import Candidate

def process_guess(state: State, guess, feedback) -> State:
    if guess == EMPTY_GUESS: return state

    guess_letter_counts = Counter()

    # Do two passes since the absent case requires more info.
    for i, ch in enumerate(feedback):
        letter = guess[i]
        guess_candidate = Candidate(letter, i)
        if CORRECT == ch:
            # Remove other candidate letters at this index.
            state = state._replace(
                candidates = set(itertools.filterfalse(
                    different_letter_same_index(guess_candidate),
                    state.candidates)),
                correct_candidates = state.correct_candidates.union({guess_candidate}),
                )
            guess_letter_counts[letter] += 1
#             state.letter_counts.update(letter)
        elif PRESENT == ch:
            # Remove this letter at this index.
            state = state._replace(
                candidates = set([x for x in state.candidates if x != (letter, i)]))
            guess_letter_counts[letter] += 1
        elif ABSENT == ch:
            pass
        else:
            raise Exception()

    state = state._replace(
        min_letter_counts = state.min_letter_counts | guess_letter_counts)

    for i, ch in enumerate(feedback):
        letter = guess[i]
        guess_candidate = Candidate(letter, i)
        if ABSENT == ch:
            if state.min_letter_counts[letter] > 0:
                # TODO: Handle better.
                # Remove this letter at this index.
                state = state._replace(
                    candidates = set([x for x in state.candidates if x != (letter, i)]))
                pass
            else:
                state = state._replace(
                    candidates = set(itertools.filterfalse(
                        same_letter(guess_candidate),
                        state.candidates)),
                )
        else:
            pass

#     print(len(state.candidates), state.candidates)

    return state


def is_eligible_word(word: str, state: State) -> bool:
    candidates = to_candidates(word)
    eligible_candidates = state.candidates & candidates
    if (len(eligible_candidates) != 5): return False

    word_letter_count = Counter(word)
    for letter, count in state.min_letter_counts.items():
        if word_letter_count[letter] < count: return False

    return True