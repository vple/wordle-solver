import string
import itertools
from filters import *
from collections import Counter
from copy import deepcopy
import typing

CORRECT = '3'
PRESENT = '2'
ABSENT = '1'

EMPTY_GUESS = '-----'

'''
Fetches wordlist and caches it as a global.
'''
g_wordlist = None
def get_wordlist():
    global g_wordlist
    if None == g_wordlist:
        g_wordlist = []
        for i in open('wordlist.txt').readlines():
            i = i[:-1]
            g_wordlist.append(i)
    return g_wordlist

def to_candidates(word: str) -> typing.Set[Candidate]:
    candidates = set()
    for i, ch in enumerate(word):
        candidates.add(Candidate(ch, i))
    return candidates

def letter_frequency_distribution(dictionary: typing.List[str]):
    counts = Counter()
    for word in dictionary:
        counts.update(word)
    return counts