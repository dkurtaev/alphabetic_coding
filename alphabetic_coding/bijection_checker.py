"""This module provides function for check coding bijection"""
from collections import deque

from alphabetic_coding.coding_tree import CodingTree


def check_bijection(codes):
    """Check bijection of coding with passed binary sequences. If coding is not
    bijective returns two different sets of codes which conctatinations are
    equals."""
    coding_tree = CodingTree()
    for code in codes:
        coding_tree.add_node(code, code)

    states = deque([State(code, [], [code]) for code in codes])
    visited_deficits = set([])
    while len(states) > 0:
        state = states.popleft()
        codes_above_deficit, codes_below_deficit = \
                coding_tree.get_neighbors(state.deficit)

        for code in codes_above_deficit + codes_below_deficit:
            next_state = state.compensate_deficit(code)

            if next_state.deficit != '':
                if next_state.deficit not in visited_deficits:
                    states.append(next_state)
                    visited_deficits.add(next_state.deficit)
            elif len(next_state.upper_word) > 1 or \
                 len(next_state.lower_word) > 1:
                return False, next_state.upper_word, next_state.lower_word

    return True, None, None


class State(object):

    def __init__(self, deficit, upper_word, lower_word):
        self.deficit = deficit
        self.upper_word = upper_word
        self.lower_word = lower_word

    def compensate_deficit(self, sequence):
        if len(sequence) > len(self.deficit):
            return State(deficit=sequence[len(self.deficit):],
                         upper_word=self.lower_word,
                         lower_word=self.upper_word + [sequence])
        else:
            return State(deficit=self.deficit[len(sequence):],
                         upper_word=self.upper_word + [sequence],
                         lower_word=self.lower_word)
