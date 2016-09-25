import unittest

from code_generator import gen_code, max_num_characters, min_code_length, \
                           max_code_length
from bijective_checker import BijectiveChecker

class TestBijectiveChecker(unittest.TestCase):

    def test_mcmillan_inequality(self):
        """Test that if coding is bijective then mcmillan inequality is true"""
        for M in range(2, 6):
            N_max = max_num_characters(M)
            for N in range(2, N_max + 1):
                L_min = min_code_length(M, N)
                L_max = max_code_length(M, N)
                for L in range(L_min, L_max + 1):
                    for _ in range(25):
                        codes = gen_code(M, N, L)
                        codes = ['1', '0', '11']
                        checker = BijectiveChecker(codes)
                        if checker.check():
                            terms = [pow(2, M - len(code)) for code in codes]
                            mcmillan_value = sum(terms)
                            self.assertLessEqual(mcmillan_value, pow(2, M))

if __name__ == '__main__':
    unittest.main()
