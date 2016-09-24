from collections import deque

class CodingTree(object):
    """This class used for building coding tree - binary tree with data about
    alphabetic coding. Each node - some binary sequence. Each left edge - '0'
    bit appending, each right edge - '1' bit appending.
             ( )
           ___|___
          |       |             sample coding table:
        ( 0 )    ( )          {'a': 11, 'b': 0, 'c': 001, 'd': 101}
       ___|    ___|___
      |       |       |
     ( )     ( )    ( 11 )
      |___    |___
          |       |
       ( 001 ) ( 101 )

    If node is not empty - we have some character whit corresponding code."""

    def __init__(self):
        self.root = CodingTreeNode()

    def add_node(self, sequence, content):
        """Adding node for binary sequence"""
        node = self.root
        for bit in sequence:
            if bit == '0':
                if node.left is None:
                    node.left = CodingTreeNode()
                node = node.left
            else:
                if node.right is None:
                    node.right = CodingTreeNode()
                node = node.right
        node.content = content

    def find_node(self, sequence):
        """Returns node by sequence."""
        node = self.root
        for bit in sequence:
            node = node.left if bit == '0' else node.right
            if node is None:
                break
        return node

    def decompose(self, sequence):
        nodes_queue = deque([self.root])
        contens_queue = deque([[]])
        for bit in sequence:
            n_nodes = len(nodes_queue)
            for _ in range(n_nodes):
                node = nodes_queue.popleft()
                content = contens_queue.popleft()

                node = node.left if bit == '0' else node.right
                if node is not None:
                    nodes_queue.append(node)
                    contens_queue.append(content)
                    if node.content is not None:
                        nodes_queue.append(self.root)
                        contens_queue.append(content + [node.content])

        # Save only finish states of decomposition (at the root of coding tree).
        decompositions = []
        for node, content in zip(nodes_queue, contens_queue):
            if node is self.root:
                decompositions.append(content)

        return decompositions


class CodingTreeNode(object):

    def __init__(self, content=None):
        self.content = content
        self.left = None
        self.right = None
