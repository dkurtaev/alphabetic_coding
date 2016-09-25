from collections import deque

from coding_tree import CodingTree

class BijectionChecker(object):

    def __init__(self, codes):
        self.codes = codes
        self.coding_tree = CodingTree()
        for code in codes:
            self.coding_tree.add_node(code, code)

    def check(self):
        return self.find() == None

    def find(self):
        class State(object):

            def __init__(self, deficit, sign, upper_word=None, lower_word=None):
                self.deficit = deficit
                self.sign = sign
                self.upper_word = upper_word
                self.lower_word = lower_word

            def compensate_deficit(self, sequence):
                if len(sequence) > len(self.deficit):
                    new_deficit = sequence[len(self.deficit):]
                    new_sign = -self.sign
                else:
                    new_deficit = self.deficit[len(sequence):]
                    new_sign = self.sign

                if self.sign < 0:
                    return State(new_deficit, new_sign,
                                 upper_word=self.upper_word + [sequence],
                                 lower_word=self.lower_word)
                else:
                    return State(new_deficit, new_sign,
                                 upper_word=self.upper_word,
                                 lower_word=self.lower_word + [sequence])

            def hash(self):
                return self.sign * int('1' + self.deficit, 2)


        states = deque([State(code, -1, [], [code]) for code in self.codes])
        deficits_hashes = set([])
        while len(states) > 0:
            state = states.popleft()
            codes_above_deficit, codes_below_deficit = \
                    self.coding_tree.get_neighbors(state.deficit)

            for code in codes_above_deficit + codes_below_deficit:
                next_state = state.compensate_deficit(code)

                if next_state.deficit != '':
                    if next_state.hash() not in deficits_hashes:
                        states.append(next_state)
                        deficits_hashes.add(next_state.hash())
                elif len(next_state.upper_word) > 1 or \
                     len(next_state.lower_word) > 1:
                    return next_state.upper_word, next_state.lower_word
