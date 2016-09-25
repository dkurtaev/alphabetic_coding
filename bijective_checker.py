"""This module using for check bijection between encoded and source text via
specific coding table. Method in follows:
    *   Find set of binary sequences which are simultanously prefix and suffix
        of some elementary code. Let's call them as suprefixes (is better than
        presuffixes). Additionaly add extra empty suprefix.
        For example, for coding table with codes ['010', '100', '00', '101']
        there are ['', '0', '1', '01', '10'] (but without '00').

    *   Build a graph of decompositions where nodes corresponding to suprefixes
        and edge between s1 and s2 exists if some code [ck] has decomposition
        ck = s1 + c1 + c2 + ... + cn + s2. Where
            1. ci - codes from coding table
            2. s1 and s2 are empty if n > 1
            3. s1 or s2 is empty => s2 or s1 is not empty and n > 0.
        Resulting graph is oriented and weighted.

    *   Find a loop with node correspondings to empty suprefix. If it exists,
        coding is not bijective."""
import itertools
import re

from collections import deque

from coding_tree import CodingTree

class BijectiveChecker(object):

    def __init__(self, codes):
        self.codes = codes
        self.coding_tree = CodingTree()
        for code in codes:
            self.coding_tree.add_node(code, code)

    def check(self):
        suprefixes = self.extract_suprefixes()
        decompositions = []
        for code in self.codes:
            decompositions += self.get_decompositions(code, suprefixes)
        return self.find_loop(suprefixes, decompositions) is None

    def extract_suprefixes(self):
        """Extracting set of suprefixes: binary sequences which are prefix and
        suffix of some elementary codes. For each possible suffix we will guide
        by coding tree and add this suffix if final node exists."""
        suprefixes = ['']
        for code in self.codes:
            for suffix in [code[i:] for i in range(1, len(code))]:
                node = self.coding_tree.find_node(suffix)
                if node is not None:
                    # Check that node is not leaf.
                    if node.left is not None or node.right is not None:
                        if suffix not in suprefixes:
                            suprefixes.append(suffix)

        return suprefixes

    def get_decompositions(self, sequence, suprefixes):
        """Decompose binary sequence to set of words s1, c1, ..., cn, s2 Where
        s1, s2 from suprefixes, ck are code"""
        decompositions = []
        for prefix, suffix in itertools.product(suprefixes, suprefixes):
            if sequence[:-1].startswith(prefix) and \
               sequence[1:].endswith(suffix):
                if len(sequence) > len(prefix) + len(suffix):
                    middle_part = re.sub(r'^%s' % prefix, r'', sequence)
                    middle_part = re.sub(r'%s$' % suffix, r'', middle_part)
                    for d in self.coding_tree.decompose(middle_part):
                        if prefix != '' and suffix != '' and len(d) > 0 or \
                           prefix == '' and suffix != '' and len(d) > 0 or \
                           prefix != '' and suffix == '' and len(d) > 0 or \
                           prefix == '' and suffix == '' and len(d) > 1:
                            decompositions.append([prefix] + d + [suffix])
                elif len(sequence) == len(prefix) + len(suffix):
                    decompositions.append([prefix, '', suffix])

        return decompositions

    def find_loop(self, suprefixes, decompositions):
        class Edge(object):

            def __init__(self, to, weight):
                self.to = to
                self.weight = ''.join(weight)

        visited = {s: False for s in suprefixes}

        edges = {s: [] for s in suprefixes}
        for d in decompositions:
            node_from = d[0]
            node_to = d[-1]
            weight = d[1:-1]
            edges[node_from].append(Edge(node_to, weight))

        nodes_queue = deque([''])
        texts_queue = deque([''])
        while len(nodes_queue) > 0:
            n_nodes = len(nodes_queue)
            for _ in range(n_nodes):
                node = nodes_queue.popleft()
                text = texts_queue.popleft()
                for edge in edges[node]:
                    if not visited[edge.to]:
                        nodes_queue.append(edge.to)
                        if edge.to != '':
                            texts_queue.append(text + edge.weight + edge.to)
                            visited[edge.to] = True
                        else:
                            return text + edge.weight

        return None
