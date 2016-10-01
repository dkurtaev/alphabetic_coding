from test_coding import TestCoding
from alphabetic_coding.huffman_coding import encode_huffman
from alphabetic_coding.custom_coding import encode_custom, decode_custom

class TestCustomCoding(TestCoding):

    @classmethod
    def setUpClass(self):
        print '\nTestCustomCoding'

    def test_decode_encoded_via_huffman(self):
        for _ in range(1000):
            text = self.gen_text()
            encoded_text, coding_table = encode_huffman(text)
            decoded_text = decode_custom(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)

    def test_encoder(self):
        for _ in range(1000):
            text = self.gen_text()
            encoded_text, coding_table = encode_huffman(text)
            custom_encoded_text = encode_custom(text, coding_table)
            self.assertEqual(custom_encoded_text, encoded_text)
