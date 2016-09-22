class BSTNode(object):

    def __init__(self, key, content=None):
        self.key = key
        self.content = content
        self.left = None
        self.right = None

    def print_node(self, print_offset=''):
        print '%s|--' % print_offset, self.key, self.content

        if self.left is not None:
            self.left.print_node('%s    ' % print_offset)
        else:
            print('%s    |-- None' % print_offset)

        if self.right is not None:
            self.right.print_node('%s    ' % print_offset)
        else:
            print('%s    |-- None' % print_offset)


class BST(object):

    def __init__(self):
        self.root = None

    def add_node(self, key, content=None):
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
