import unittest

from code_generator import gen_code, max_num_characters, min_code_length, \
                           max_code_length

class TestCodeGenerator(unittest.TestCase):

    def test_gen_lengths(self):
        for M in range(2, 6):
            N_max = max_num_characters(M)
            for N in range(2, N_max + 1):
                L_min = min_code_length(M, N)
                L_max = max_code_length(M, N)
                for L in range(L_min, L_max + 1):
                    for _ in range(10):
                        code = gen_code(M, N, L)
                        lengths = [len(c) for c in code]
                        self.assertEqual(max(lengths), M)
                        self.assertEqual(len(lengths), N)
                        self.assertEqual(sum(lengths), L)

if __name__ == '__main__':
    random.seed(324)
    unittest.main()
