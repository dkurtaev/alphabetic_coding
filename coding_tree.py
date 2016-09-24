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


class CodingTreeNode(object):

    def __init__(self, content=None):
        self.content = content
        self.left = None
        self.right = None
