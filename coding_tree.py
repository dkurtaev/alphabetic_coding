from coding_tree_node import CodingTreeNode

class CodingTree(object):

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
