import unittest

from code_generator import gen_lengths, max_num_characters, min_code_length, \
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
                        x = gen_lengths(M, N, L)
                        self.assertEqual(len(x), M)
                        self.assertEqual(sum(x), N)
                        x = [x[i] * (i + 1) for i in range(0, M)]
                        self.assertEqual(sum(x), L)


if __name__ == '__main__':
    random.seed(324)
    unittest.main()
