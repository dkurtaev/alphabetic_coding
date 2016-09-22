from binary_search_tree import BST
from coding_tree import CodingTree

class HuffmanEncoder(object):
    """ Huffman encoding - method gives optimal prefix coding using frequence of
    characters in source text: more frequent characters has more shorter code.
    """

    def encode(self, text):
        """Encoding source text into binary sequence."""
        coding_table = self.get_coding_table(text)
        return ''.join(coding_table[char] for char in text)

    def get_coding_table(self, text):
        """Returns dictionary {'character': binary code}."""
        counts_table = self.get_counts_table(text)
        coding_table = {char: '' for char in counts_table}

        tree = BST()
        for char, count in counts_table.items():
            tree.add_node(key=count, content=[char])

        # Each iteration deletes one node.
        for iteration in range(len(counts_table) - 1):
            nodes = [tree.pop_min_key_node(), tree.pop_min_key_node()]

            for i, node in enumerate(nodes):
                for char in node.content:
                    coding_table[char] = '%d%s' % (i, coding_table[char])

            tree.add_node(key=nodes[0].key + nodes[1].key,
                          content=nodes[0].content + nodes[1].content)

        return coding_table

    def get_counts_table(self, text):
        """Returns dictionary {'character': number of it in text}."""
        counts_table = {}
        for char in text:
            counts_table[char] = counts_table.get(char, 0) + 1

        return counts_table


class HuffmanDecoder(object):
    """ Decoding binary sequence received with Huffman encoding."""

    def decode(self, sequence, coding_table):
        """Decoding binary sequence into text."""
        coding_tree = CodingTree()
        for char, code in coding_table.items():
            coding_tree.add_node(code, char)

        text = ''
        i = 0
        while i < len(sequence):
            node = coding_tree.root
            while node.content == None:
                node = node.left if sequence[i] == '0' else node.right
                i += 1
            text += node.content
        return text
