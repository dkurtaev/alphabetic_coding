from coding_tree import CodingTree

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
