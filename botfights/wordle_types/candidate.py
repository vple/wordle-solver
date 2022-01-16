import string
from typing import NamedTuple, Set

class Candidate(NamedTuple):
    letter: str
    index: int

g_base_candidates: Set[Candidate] = None
def get_base_candidates() -> Set[Candidate]:
    global g_base_candidates
    if None == g_base_candidates:
        g_base_candidates = set()
        for letter in string.ascii_lowercase:
            for i in range(5):
                g_base_candidates.add((letter, i))
    return g_base_candidates