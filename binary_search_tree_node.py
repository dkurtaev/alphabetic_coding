import sys

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
