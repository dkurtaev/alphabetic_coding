import unittest
import random

from string import whitespace, digits, letters, punctuation

from huffman_coding import HuffmanEncoder
from custom_coding import Decoder

class TestCustomCoding(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCustomCoding, self).__init__(*args, **kwargs)
        random.seed(324)
        self.text_seed = whitespace + digits + letters + punctuation

    def gen_text(self):
        length = random.randint(2, 25)
        return ''.join(random.choice(self.text_seed) for j in range(length))

    def test_decode_encoded_via_huffman(self):
        for gen in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)
            encoded_text = HuffmanEncoder().encode(text)
            decoded_text = Decoder().decode(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)

if __name__ == '__main__':
    unittest.main()
