from test_coding import TestCoding
from test_code_generator import gen_loop
from bijection_checker import BijectionChecker
from huffman_coding import HuffmanEncoder

class TestBijectionChecker(TestCoding):

    def test_mcmillan_inequality(self):
        """Test that if coding is bijective then mcmillan inequality is true"""
        print '\rTestBijectionChecker.test_mcmillan_inequality'
        def test(M, N, L, codes):
            checker = BijectionChecker(codes)
            if checker.check():
                terms = [pow(2, M - len(code)) for code in codes]
                mcmillan_value = sum(terms)
                self.assertLessEqual(mcmillan_value, pow(2, M))

        gen_loop(test)

    def test_bijection_for_huffman_codes(self):
        """Huffman coding is a prefix coding. Prefix codes are bijective."""
        print '\rTestBijectionChecker.test_bijection_for_huffman_codes'
        for _ in range(1000):
            text = self.gen_text()
            coding_table = HuffmanEncoder().get_coding_table(text)
            checker = BijectionChecker(coding_table.values())
            self.assertTrue(checker.check())
