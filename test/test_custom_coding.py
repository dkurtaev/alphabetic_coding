from test_coding import TestCoding
from huffman_coding import HuffmanEncoder
from custom_coding import Decoder

class TestCustomCoding(TestCoding):

    def test_decode_encoded_via_huffman(self):
        for gen in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)
            encoded_text = HuffmanEncoder().encode(text)
            decoded_text = Decoder().decode(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)
