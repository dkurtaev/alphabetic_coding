import unittest
import random

from string import whitespace, digits, letters, punctuation

class TestCoding(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCoding, self).__init__(*args, **kwargs)
        random.seed(324)
        self.text_seed = whitespace + digits + letters + punctuation

    def gen_text(self):
        length = random.randint(2, 25)
        return ''.join(random.choice(self.text_seed) for j in range(length))

if __name__ == '__main__':
    unittest.main()
