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

        states = deque([State(code, -1, [], [code]) for code in self.codes])
        visited_pos = []
        visited_neg = []
        while len(states) > 0:
            state = states.popleft()
            codes_above_deficit, codes_below_deficit = \
                    self.coding_tree.get_neighbors(state.deficit)

            next_states = []
            for code in codes_above_deficit:
                # deficit = (code)...
                next_states.append(State(deficit=state.deficit[len(code):],
                                         sign=state.sign))
            for code in codes_below_deficit:
                # code = (deficit)...
                next_states.append(State(deficit=code[len(state.deficit):],
                                         sign=state.sign * -1))

            for next_state in next_states:
                deficit_is_visited = True

                if next_state.sign == 1:
                    if next_state.deficit not in visited_pos:
                        deficit_is_visited = False
                        visited_pos.append(next_state.deficit)
                else:
                    if next_state.deficit not in visited_neg:
                        deficit_is_visited = False
                        visited_neg.append(next_state.deficit)

                if not deficit_is_visited:
                    if state.sign == 1:
                        next_state.upper_word = state.upper_word
                        next_state.lower_word = state.lower_word + [code]
                    else:
                        next_state.upper_word = state.upper_word + [code]
                        next_state.lower_word = state.lower_word

                    if next_state.deficit != '':
                        states.append(next_state)
                    elif len(next_state.upper_word) > 1 or \
                         len(next_state.lower_word) > 1:
                        return next_state.upper_word, next_state.lower_word
