import unittest

from code_generator import gen_code, max_num_characters, min_code_length, \
                           max_code_length

class TestCodeGenerator(unittest.TestCase):

    def gen_loop(self, test):
        for M in range(2, 6):
            N_max = max_num_characters(M)
            for N in range(2, N_max + 1):
                L_min = min_code_length(M, N)
                L_max = max_code_length(M, N)
                for L in range(L_min, L_max + 1):
                    for _ in range(10):
                        codes = gen_code(M, N, L)
                        test(M, N, L, codes)

    def test_gen_lengths(self):
        def test(M, N, L, codes):
            lengths = [len(code) for code in codes]
            self.assertEqual(max(lengths), M)
            self.assertEqual(len(lengths), N)
            self.assertEqual(sum(lengths), L)

        self.gen_loop(test)

    def test_codes_uniquness(self):
        def test(M, N, L, codes):
            self.assertEqual(len(codes), len(set(codes)))

        self.gen_loop(test)


if __name__ == '__main__':
    random.seed(324)
    unittest.main()
