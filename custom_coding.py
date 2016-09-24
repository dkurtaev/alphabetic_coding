import re

from collections import deque

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
            for char in text:
                assert char in self.coding_table, \
                    'All characters in text must be mapped to binary sequences'
        return ''.join(self.coding_table[char] for char in text)


class Decoder(object):

    def decode(self, sequence, coding_table):
        coding_tree = CodingTree()
        for char, code in coding_table.items():
            coding_tree.add_node(code, char)

        nodes_queue = deque([coding_tree.root])
        texts_queue = deque([''])
        for bit in sequence:
            n_nodes = len(nodes_queue)
            for _ in range(n_nodes):
                node = nodes_queue.popleft()
                text = texts_queue.popleft()

                node = node.left if bit == '0' else node.right
                if node is not None:
                    if node.content is None:
                        nodes_queue.append(node)
                        texts_queue.append(text)
                    else:
                        nodes_queue.append(node)
                        texts_queue.append(text + node.content)
                        nodes_queue.append(coding_tree.root)
                        texts_queue.append(text + node.content)

        return texts_queue.popleft()
