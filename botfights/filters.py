from wordle_types.candidate import Candidate

def same_letter(candidate: Candidate):
    return lambda x: x[0] == candidate.letter

def different_letter(candidate: Candidate):
    return lambda x: x[0] != candidate.letter

def different_letter_same_index(candidate: Candidate):
    return lambda x: x[0] != candidate.letter and x[1] == candidate.index
