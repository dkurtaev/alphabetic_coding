class HuffmanEncoder(object):
    """ Hufman encoding - method gives optimal prefix coding using frequence of
    characters in source text: more frequent characters has more shorter code.
    """

    def encode(self, str):
        counts_table = self.get_counts(str)

        tree = [[count, [char]] for char, count in counts_table.iteritems()]
        for char in counts_table:
            counts_table[char] = ''

        while len(tree) > 1:
            tree.sort(key=lambda node: node[0])
            nodes = tree[0:2]
            del tree[0:2]

            for i, node in enumerate(nodes):
                for char in node[1]:
                    counts_table[char] = '%d%s' % (i, counts_table[char])

            tree.append([nodes[0][0] + nodes[1][0],
                         nodes[0][1] + nodes[1][1]])

        return counts_table

    def get_counts(self, text):
        """Returns dictionary with pairs 'character': number of it in text."""
        counts_table = {}
        for char in text:
            counts_table[char] = counts_table.get(char, 0) + 1

        return counts_table
