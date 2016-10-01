"""Huffman encoding - method which gives optimal prefix coding using frequences
of characters in source text: more frequent characters has more shorter codes.
"""
from collections import Counter

from alphabetic_coding.binary_search_tree import BST
from alphabetic_coding.coding_tree import CodingTree

def encode_huffman(text):
    """Encoding source text into binary sequence."""
    coding_table = huffman_coding_table(text)
    encoded_text = ''.join(coding_table[char] for char in text)
    return encoded_text, coding_table

def huffman_coding_table(text):
    """Returns dictionary {'character': 'binary code'}."""
    counts_table = dict(Counter(text))
    coding_table = {char: '' for char in counts_table}

    # Exceptional case.
    if len(coding_table) == 1:
        coding_table[coding_table.keys()[0]] = '0'
        return coding_table

    tree = BST()
    for char, count in counts_table.items():
        tree.add_node(key=count, content=[char])

    # Each iteration deletes one node.
    for _ in range(len(counts_table) - 1):
        nodes = [tree.pop_min_key_node(), tree.pop_min_key_node()]

        for i, node in enumerate(nodes):
            for char in node.content:
                coding_table[char] = '%d%s' % (i, coding_table[char])

        tree.add_node(key=nodes[0].key + nodes[1].key,
                      content=nodes[0].content + nodes[1].content)

    return coding_table

def decode_huffman(sequence, coding_table):
    """Decoding binary sequence received with Huffman encoding."""
    coding_tree = CodingTree()
    for char, code in coding_table.items():
        coding_tree.add_node(code, char)

    text = ''
    node = coding_tree.root
    for bit in sequence:
        node = node.left if bit == '0' else node.right
        if node.content is not None:
            text += node.content
            node = coding_tree.root

    return text
