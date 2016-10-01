from test_coding import TestCoding
from test_code_generator import gen_loop
from bijection_checker import check_bijection
from huffman_coding import huffman_coding_table
from code_generator import gen_unbijective_coding

class TestBijectionChecker(TestCoding):

    @classmethod
    def setUpClass(self):
        print '\nTestBijectionChecker'

    def test_mcmillan_inequality(self):
        """Test that if coding is bijective then mcmillan inequality is true"""
        def test(M, N, L, codes):
            is_bijective, _, _ = check_bijection(codes)
            if is_bijective:
                terms = [pow(2, M - len(code)) for code in codes]
                mcmillan_value = sum(terms)
                self.assertLessEqual(mcmillan_value, pow(2, M))

        gen_loop(test)

    def test_bijection_for_huffman_codes(self):
        """Huffman coding is a prefix coding. Prefix codes are bijective."""
        for _ in range(1000):
            text = self.gen_text()
            coding_table = huffman_coding_table(text)
            is_bijective, _, _ = check_bijection(coding_table.values())
            self.assertTrue(is_bijective)

    def test_checker_output(self):
        """If coding is not bijective, checker returns pair of codes which
        encoding equally."""
        def test(M, N, L, codes):
            is_bijective, first_word, second_word = check_bijection(codes)
            if not is_bijective:
                self.assertGreater(len(first_word), 0)
                self.assertGreater(len(second_word), 0)
                for code in first_word + second_word:
                    self.assertIn(code, codes)
                self.assertNotEqual(first_word, second_word)
                self.assertEqual(''.join(first_word), ''.join(second_word))

        gen_loop(test)

    def test_unbijective_codes(self):
        """Generate guaranteed not bijective coding. Checker should recognize
        them as not bijective."""
        for _ in range(10000):
            codes = gen_unbijective_coding()
            is_bijective, _, _ = check_bijection(codes)
            self.assertFalse(is_bijective)
