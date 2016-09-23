class BST(object):
    """BST (Binary Search Tree) - data structure for organize data by keys.
    Keys should be comparable. Each node of tree has content and references
    to node with greater key (right) and lesser key (left)"""

    def __init__(self):
        self.root = None

    def add_node(self, key, content=None):
        """Adding new node in right position. Average labor intensity is
        O(log_2(n)), where n - current number of nodes. This is because each
        keys comparison guides to subtree with half of power of nodes.
        Balanced tree has depth less or equal log_2(n), maximal depth of
        unbalanced tree is n (linear list)"""
        if self.root is None:
            self.root = BSTNode(key, content)
            return

        node = self.root
        while True:
            if key < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = BSTNode(key, content)
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = BSTNode(key, content)
                    break

    def pop_min_key_node(self):
        """Find and delete node with minimal key"""
        if self.root is not None:
            node = self.root
            parent = self.root
            while node.left is not None:
                parent = node
                node = node.left
            if node is not self.root:
                parent.left = node.right
            else:
                self.root = self.root.right
            return node

    def print_tree(self):
        self.root.print_node()


class BSTNode(object):

    def __init__(self, key, content=None):
        self.key = key
        self.content = content
        self.left = None
        self.right = None

    def print_node(self, print_offset=''):
        """Printing node info in format
        ***|-- key, content
        ***    left node printing with offset '***    '
        ***    right node pringint with offset '***    '
        Here is the *** of offset from parent's node.
        Printing None if child node is not presented.
        """
        print '%s|--' % print_offset, self.key, self.content

        if self.left is not None:
            self.left.print_node('%s    ' % print_offset)
        else:
            print '%s    |-- None' % print_offset

        if self.right is not None:
            self.right.print_node('%s    ' % print_offset)
        else:
            print '%s    |-- None' % print_offset
