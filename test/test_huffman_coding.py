from collections import Counter
from math import log

from test_coding import TestCoding
from huffman_coding import HuffmanEncoder, HuffmanDecoder

class TestHuffmanCoding(TestCoding):

    @classmethod
    def setUpClass(self):
        print '\nTestHuffmanCoding'

    def test_all_chars_used(self):
        for _ in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            for char in text:
                self.assertIn(char, scheme)

    def test_codes_are_binary(self):
        for _ in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            for code in scheme.values():
                self.assertRegexpMatches(code, r'^[01]+$')

    def test_coding_are_prefix(self):
        for _ in range(1000):
            text = self.gen_text()
            scheme = HuffmanEncoder().get_coding_table(text)
            codes = scheme.values()
            for i in range(len(codes) - 1):
                for j in range(i + 1, len(codes)):
                    self.assertFalse(codes[i].startswith(codes[j]))
                    self.assertFalse(codes[j].startswith(codes[i]))

    def test_decode_encoded(self):
        for _ in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)
            encoded_text = HuffmanEncoder().encode(text)
            decoded_text = HuffmanDecoder().decode(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)

    def test_entropy(self):
        for gen in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)

            counts = dict(Counter(text))
            cost = 0
            entropy = 0
            for char, code in coding_table.items():
                freq = float(counts[char]) / len(text)
                entropy -= freq * log(freq, 2)
                cost += len(code) * freq

            self.assertLessEqual(entropy, cost)
            self.assertLessEqual(cost, entropy + 1)
