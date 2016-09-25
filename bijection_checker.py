from collections import deque

class BijectionChecker(object):

    def __init__(self, codes):
        self.codes = codes

    def check(self):
        return self.find() == None

    def find(self):
        states = []
        for code in self.codes:
            states.append({
                'deficit': code,
                'sign': -1,
                'upper_word': [],
                'lower_word': [code]})
        states = deque(states)

        visited_pos = []
        visited_neg = []
        while len(states) > 0:
            state = states.popleft()
            for code in self.codes:
                next_state = None
                if state['deficit'].startswith(code):
                    next_state = {
                        'deficit': state['deficit'][len(code):],
                        'sign': state['sign'],
                        'upper_word': state['upper_word'] if state['sign'] == 1 else state['upper_word'] + [code],
                        'lower_word': state['lower_word'] if state['sign'] == -1 else state['lower_word'] + [code]
                    }
                elif code.startswith(state['deficit']):
                    next_state = {
                        'deficit': code[len(state['deficit']):],
                        'sign': state['sign'] * -1,
                        'upper_word': state['upper_word'] if state['sign'] == 1 else state['upper_word'] + [code],
                        'lower_word': state['lower_word'] if state['sign'] == -1 else state['lower_word'] + [code]
                    }
                if next_state is not None:
                    cont = False
                    if next_state['sign'] == 1:
                        if next_state['deficit'] not in visited_pos:
                            cont = True
                            visited_pos.append(next_state['deficit'])
                    else:
                        if next_state['deficit'] not in visited_neg:
                            cont = True
                            visited_neg.append(next_state['deficit'])
                    if cont:
                        if next_state['deficit'] != '':
                            states.append(next_state)
                        elif len(next_state['upper_word']) > 1 or len(next_state['lower_word']) > 1:
                            return next_state['upper_word'], next_state['lower_word']
