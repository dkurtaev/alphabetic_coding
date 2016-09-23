import unittest
import random

from string import whitespace, digits, letters, punctuation

from huffman_coding import HuffmanEncoder, HuffmanDecoder


class TestHuffmanCoding(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestHuffmanCoding, self).__init__(*args, **kwargs)
        random.seed(324)
        self.text_seed = whitespace + digits + letters + punctuation

    def gen_text(self):
        length = random.randint(2, 25)
        return ''.join(random.choice(self.text_seed) for j in range(length))

    def test_all_chars_used(self):
        for gen in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            for char in text:
                self.assertIn(char, scheme)

    def test_codes_are_binary(self):
        for gen in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            for code in scheme.values():
                self.assertRegexpMatches(code, r'^[01]+$')

    def test_coding_are_prefix(self):
        for gen in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            codes = scheme.values()
            for i in range(len(codes) - 1):
                for j in range(i + 1, len(codes)):
                    self.assertFalse(codes[i].startswith(codes[j]))
                    self.assertFalse(codes[j].startswith(codes[i]))

    def test_decoder(self):
        for gen in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)
            encoded_text = HuffmanEncoder().encode(text)
            decoded_text = HuffmanDecoder().decode(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)

if __name__ == '__main__':
    unittest.main()
