import unittest
import random

from binary_search_tree import BST


class TestBST(unittest.TestCase):

    def test_fuzz(self):
        random.seed(324)
        tree = BST()
        for i in range(1000):
            if random.randint(0, 1):
                tree.add_node(random.random())
            else:
                tree.pop_min_key_node()

if __name__ == '__main__':
    unittest.main()
