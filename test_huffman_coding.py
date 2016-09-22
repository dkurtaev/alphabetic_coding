import unittest

from huffman_coding import HuffmanEncoder, HuffmanDecoder


class TestHuffmanCoding(unittest.TestCase):

    def test_all_chars_used(self):
        text = 'my little string'
        scheme = HuffmanEncoder().get_coding_table(text)
        for char in text:
            self.assertIn(char, scheme)

    def test_codes_are_binary(self):
        text = 'my little string'
        scheme = HuffmanEncoder().get_coding_table(text)
        for code in scheme.values():
            self.assertRegexpMatches(code, r'^[01]+$')

    def test_coding_are_prefix(self):
        text = 'my little string'
        scheme = HuffmanEncoder().get_coding_table(text)
        codes = scheme.values()
        for i in range(len(codes) - 1):
            for j in range(i + 1, len(codes)):
                self.assertFalse(codes[i].startswith(codes[j]))
                self.assertFalse(codes[j].startswith(codes[i]))

if __name__ == '__main__':
    unittest.main()
