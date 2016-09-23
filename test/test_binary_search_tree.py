import unittest
import numpy as np

from binary_search_tree import BST


class TestBST(unittest.TestCase):

    def test_fuzz(self):
        np.random.seed(324)
        tree = BST()
        for i in range(1000):
            if np.random.randint(0, 2):
                tree.add_node(key=np.random.rand())
            else:
                tree.pop_min_key_node()

    def test_pop_min_key(self):
        np.random.seed(324)
        tree = BST()
        values = np.random.randint(low=0, high=100, size=1000)
        for value in values:
            tree.add_node(key=value)

        for value in sorted(values):
            self.assertEqual(value, tree.pop_min_key_node().key)


if __name__ == '__main__':
    unittest.main()
