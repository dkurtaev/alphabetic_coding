"""Huffman encoding - method which gives optimal prefix coding using frequences
of characters in source text: more frequent characters has more shorter codes.
"""
from collections import Counter
from heapq import heapify, heappush, heappop

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

    heap = [(count, [char]) for char, count in counts_table.items()]
    heapify(heap)

    # Each iteration deletes one node.
    for _ in range(len(counts_table) - 1):
        nodes = [heappop(heap), heappop(heap)]

        for i, node in enumerate(nodes):
            for char in node[1]:
                coding_table[char] = '%d%s' % (i, coding_table[char])

        heappush(heap, (nodes[0][0] + nodes[1][0],   # Add counts.
                        nodes[0][1] + nodes[1][1]))  # Merge characters.

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
