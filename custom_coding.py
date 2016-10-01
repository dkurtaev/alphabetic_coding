import re

from coding_tree import CodingTree

class Encoder(object):

    def __init__(self, coding_table, debug=True):
        self.coding_table = coding_table
        if debug:
            for code in coding_table.values():
                assert re.search(r'^[01]+$', code) != None, \
                    'All codes must be binary'

    def encode(self, text, debug=True):
        """Encode source text into binary sequence using custom coding table."""
        if debug:
            assert all(char in self.coding_table for char in text), \
                'All characters in text must be mapped to binary sequences'
        return ''.join(self.coding_table[char] for char in text)


class Decoder(object):

    def decode(self, sequence, coding_table):
        coding_tree = CodingTree()
        for char, code in coding_table.items():
            coding_tree.add_node(code, char)

        decompositions = coding_tree.decompose(sequence)
        assert len(decompositions) < 2, 'Coding is not bijective.'
        assert len(decompositions) > 0, 'Wrong coding table.'
        return ''.join(decompositions[0])
