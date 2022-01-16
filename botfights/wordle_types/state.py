import collections
import string
import typing

from utils import *
from wordle_types.candidate import *

def to_candidates(word: str) -> typing.Set[Candidate]:
    candidates = set()
    for i, ch in enumerate(word):
        candidates.add(Candidate(ch, i))
    return candidates

class State(typing.NamedTuple):
    candidates: typing.Set[Candidate] = get_base_candidates()
    correct_candidates: typing.Set[Candidate] = set()
    min_letter_counts: typing.Counter[str] = collections.Counter()

    def is_eligible_word(self, word: str) -> bool:
        candidates = to_candidates(word)
        eligible_candidates = self.candidates & candidates
        if (len(eligible_candidates) != 5): return False

        word_letter_count = Counter(word)
        for letter, count in self.min_letter_counts.items():
            if word_letter_count[letter] < count: return False

        return True

#     _eligible_words = None
    def eligible_words(self, dictionary: typing.List[str] = get_wordlist()) -> typing.List[str]:
#         if self._eligible_words == None:
#             self._eligible_words = list(filter(lambda x: self.is_eligible_word(x), dictionary))
#         return self._eligible_words
        return list(filter(lambda x: self.is_eligible_word(x), dictionary))

