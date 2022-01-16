import random

from utils import *
from state_utils import *
from wordle_types.state import State

# sample-bot.py

# sample bot to play wordle. see wordle.py for how to play.


# this has lots of false positives, only pay attention to 3s
#
def could_match(target, guess, feedback):
    for i, ch in enumerate(feedback):
        if '3' == ch:
            if target[i] != guess[i]:
                return False
        else:
            if target[i] == guess[i]:
                return False
    return True

def play(guess_state):
    dictionary = get_wordlist()
    eligible_words = get_wordlist()

    # guess_state looks like: "-----:00000,arose:31112,amend:31211"
    # Compute state resulting from guesses.
    state = State()
    for pair in guess_state.split(','):
        guess, feedback = pair.split(':')
        state = process_guess(state, guess, feedback)

    # TODO: First guess is very slow.
    if len(state.candidates) == 130:
        return 'arose'

    eligible_words = state.eligible_words(eligible_words)
    eligible_frequency_distribution = letter_frequency_distribution(eligible_words)

#     print(eligible_frequency_distribution)


#     print(len(state.candidates))
#     guess = max(
#         dictionary,
#         key = lambda x: score_unique_distribution(state, x, eligible_frequency_distribution))

#     guess = guess_by_dictionary_score(state, dictionary, eligible_words, eligible_frequency_distribution)
    guess = guess_by_eligible_score(state, eligible_words, eligible_frequency_distribution)

#     max(
#         dictionary,
#         key = lambda x: (1 if x in eligible_words else 0) + score_unique_distribution(state, x, eligible_frequency_distribution))

#     if len(eligible_words) < 30:
#         print(eligible_words)
#     print(guess, (1 if guess in eligible_words else 0))
#     print(guess)

#     return random.choice(eligible_words)
    return guess

def guess_by_dictionary_score(state, dictionary, eligible_words, eligible_frequency_distribution):
    return max(
        dictionary,
        key = lambda x: (1 if x in eligible_words else 0) + score_unique_distribution(state, x, eligible_frequency_distribution))

def guess_by_eligible_score(state, eligible_words, eligible_frequency_distribution):
    return max(
        eligible_words,
        key = lambda x: score_unique_distribution(state, x, eligible_frequency_distribution))

def score_unique_distribution(state, guess, eligible_frequency_distribution):
    unique_letters = set(guess)

    score = 1
    for letter in unique_letters:
        if letter in state.min_letter_counts.keys():
            score *= 2
            continue
        score *= eligible_frequency_distribution[letter]

    return score