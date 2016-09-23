import unittest
import string
import random

from huffman_coding import HuffmanEncoder, HuffmanDecoder


class TestHuffmanCoding(unittest.TestCase):

    def gen_text(self):
        text_length = random.randint(2, 25)
        return ''.join(random.choice(text_seed) for j in range(text_length))

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
    random.seed(324)
    text_seed = ' ' + string.digits + string.letters + string.punctuation
    unittest.main()
