from test_coding import TestCoding
from huffman_coding import encode_huffman
from custom_coding import Decoder

class TestCustomCoding(TestCoding):

    @classmethod
    def setUpClass(self):
        print '\nTestCustomCoding'

    def test_decode_encoded_via_huffman(self):
        for _ in range(1000):
            text = self.gen_text()
            encoded_text, coding_table = encode_huffman(text)
            decoded_text = Decoder().decode(encoded_text, coding_table)
            self.assertEqual(text, decoded_text)
