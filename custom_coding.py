"""This module provides usage for coding source text using custom coding table.
Additionally you can check coding bijection: absence of words pair A and B which
has similar codes, f(A)=f(B), where f(*) - coding by considered coding table."""
import re

from coding_tree import CodingTree
from bijection_checker import check_bijection

def encode_custom(text, coding_table, debug=True):
    """Encode source text into binary sequence using custom coding table."""
    if debug:
        codes = coding_table.values()
        for code in codes:
            assert re.search(r'^[01]+$', code) != None, \
                'All codes must be binary'

        is_bijective, _, _ = check_bijection(codes)
        assert is_bijective

        assert all(char in coding_table for char in text), \
            'All characters in text must be mapped to binary sequences'

        return ''.join(coding_table[char] for char in text)

def decode_custom(sequence, coding_table):
    """Decoding binary sequence to string of corresponding characters."""
    coding_tree = CodingTree()
    for char, code in coding_table.items():
        coding_tree.add_node(code, char)

    decompositions = coding_tree.decompose(sequence)
    assert len(decompositions) < 2, 'Coding is not bijective.'
    assert len(decompositions) > 0, 'Wrong coding table.'
    return ''.join(decompositions[0])
