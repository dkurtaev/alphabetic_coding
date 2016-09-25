from collections import deque


class BijectionChecker(object):

    def __init__(self, codes):
        self.codes = codes

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
            for code in self.codes:
                next_state = None
                if state.deficit.startswith(code):
                    next_state = State(deficit=state.deficit[len(code):],
                                       sign=state.sign)
                elif code.startswith(state.deficit):
                    next_state = State(deficit=code[len(state.deficit):],
                                       sign=state.sign * -1)

                if next_state is not None:
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
