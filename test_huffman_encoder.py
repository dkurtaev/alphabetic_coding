import unittest

from huffman_encoder import HuffmanEncoder


class TestHuffmanEncoder(unittest.TestCase):

    def test_all_chars_used(self):
        text = 'my little string'
        scheme = HuffmanEncoder().encode(text)
        for char in text:
            self.assertIn(char, scheme)

    def test_codes_are_binary(self):
        text = 'my little string'
        scheme = HuffmanEncoder().encode(text)
        for code in scheme.values():
            self.assertRegexpMatches(code, r'^[01]+$')

    def test_coding_are_prefix(self):
        text = 'my little string'
        scheme = HuffmanEncoder().encode(text)
        codes = scheme.values()
        for i in range(len(codes) - 1):
            for j in range(i + 1, len(codes)):
                if len(codes[i]) == len(codes[j]):
                    self.assertNotEqual(codes[i], codes[j])
                elif len(codes[i]) < len(codes[j]):
                    self.assertNotEqual(codes[i], codes[j][0:len(codes[i])])
                else:
                    self.assertNotEqual(codes[j], codes[i][0:len(codes[j])])
