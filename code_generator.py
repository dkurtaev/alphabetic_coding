"""This module provides functions for generating set of unique binary codes.
Generally, each set has next parameters:
    M - maxiamal length of binary sequences
    N - number of binary sequences
    L - sum of binary sequences lengths (called as code length)."""
import random

from math import log, ceil
from bisect import bisect

def gen_code(M, N, L):
    """This function generates set of [N] binary sequences with maximal length
    [M] and sum [L] of lengths."""
    assert M >= 1
    assert 2 <= N <= max_num_characters(M)
    assert min_code_length(M, N) <= L <= max_code_length(M, N)

    counts = gen_lengths(M, N, L)
    code = []
    for i, count in enumerate(counts):
        if count > 0:
            seeds = random.sample(xrange(pow(2, i + 1)), count)
            for seed in seeds:
                code.append(bin(seed)[2:].rjust(i + 1, '0'))

    return code

def gen_lengths(M, N, L):
    """This function returns solving of task:
    x[1] + 2 * x[2] + ... + M * x[M] = L
    x[1] + x[2] + ... + x[M] = N
    0 <= x[i] <= pow(2, i), i = 1..M
    x[M] >= 1
    where x[i] interpreted as number of sequences with length i."""
    assert M >= 1
    assert 2 <= N <= max_num_characters(M)
    assert min_code_length(M, N) <= L <= max_code_length(M, N)

    x = [0 for _ in range(M)]
    x[M - 1] = 1

    # List of lenghts i for which x[i] < pow(2, i).
    not_full_lenghts = [i + 1 for i in range(M)]

    # Generate random initial lenghts distribution.
    current_L = M
    for _ in range(1, N):
        idx = random.randint(0, len(not_full_lenghts) - 1)
        length = not_full_lenghts[idx]
        x[length - 1] += 1
        if x[length - 1] == pow(2, length):
            del not_full_lenghts[idx]
        current_L += length

    # Optimization.
    while current_L != L:
        if current_L > L:
            min_dec_len = not_full_lenghts[0] + 1
            max_dec_len = M
        else:
            min_dec_len = 1
            max_dec_len = not_full_lenghts[-1] - 1

        # Select decremented length.
        dec_len = random.randint(min_dec_len, max_dec_len)
        while x[dec_len - 1] == 0 or dec_len == M and x[M - 1] == 1:
            dec_len = random.randint(min_dec_len, max_dec_len)

        # Find decremented length position at list of not full lengths.
        # Insert if not exists.
        if dec_len in not_full_lenghts:
            dec_len_id = not_full_lenghts.index(dec_len)
        else:
            dec_len_id = bisect(not_full_lenghts, dec_len)
            not_full_lenghts.insert(dec_len_id, dec_len)

        # Select incremented length.
        if current_L > L:
            inc_len_id = random.randint(0, dec_len_id - 1)
        else:
            inc_len_id = random.randint(dec_len_id + 1,
                                        len(not_full_lenghts) - 1)
        inc_len = not_full_lenghts[inc_len_id]

        x[dec_len - 1] -= 1
        x[inc_len - 1] += 1
        current_L += inc_len - dec_len
        if x[inc_len - 1] == pow(2, inc_len):
            del not_full_lenghts[inc_len_id]

    return x


def min_code_length(M, N):
    """This function returns minimal code length for specific number of
    binary sequences (N) and maximal binary sequences length (M).
    One of sequences has fixed length M.

    1.  Full powered sum:
        2 + 4 + 8 + ... + 2^x = 2 * (2^x - 1) <= N where x <= M

    2.  L_full = sum_{i=1}^{x}(i * 2^i) =
                 sum_{k=1}^{x}( sum_{i=k}^{x}(2^i) ) =
                 sum_{k=1}^{x}( 2^k * (2^{x-k+1} - 1) ) =
                 sum_{k=1}^{x}( 2^{x+1} - 2^k) =
                 x * 2^{x+1} - 2 * (2^x - 1) =
                 2^{x+1} * (x - 1) + 2

    3. L = L_full + (N - 2 * (2^x - 1)) * (x + 1) =
           2^{x+1} * (x - 1) + 2 + (N - 2^{x+1} + 2) * (x + 1) =
           2^{x+1} * (x - 1) + 2 + (N + 2) * (x + 1) - 2^{x+1} * (x + 1) =
           (N + 2) * (x + 1) + 2 - 2^{x+2}."""
    if N <= max_num_characters(M):
        m = int(log(N + 1, 2))
        return (N + 1) * m - pow(2, m + 1) + M + 2
    else:
        return 0

def max_code_length(M, N):
    """This function returns maximal code length for specific number of
    codes (N) and maximal binary sequences length (M).
    One of sequences has fixed length M.

    1.  Full powered sum:
        2^M + 2^{M-1} + ... + 2^x =
        2^x * (2^(M - x + 1) - 1) =
        = 2^{M+1} - 2^x <= N, where x >= 1.

    2.  L_full = sum_{i=x}^{M}(i * 2^i) = x * sum_{i=x}^{M}(2^i) +
                 sum_{k=x+1}^{M}( sum_{i=k}^{M}(2^i) ) =
                 x * (2^{M+1} - 2^x) + sum_{k=x+1}^{M}( 2^{M+1} - 2^k ) =
                 x * (2^{M+1} - 2^x) + 2^{M+1} * (M - x) - (2^{M+1} - 2^{x+1}) =
                 2^x * (2 - x) + 2^{M+1} * (M - 1)

    3.  L = L_full + (x - 1) * (N - 2^{M+1} + 2^x) = 2^x * (2 - x) +
        2^{M+1} * (M - 1) + (x - 1) * (N - 2^{M+1} + 2^x) =
        2^{M+1} * (M - x) + 2^x + N * (x - 1)."""
    if N <= max_num_characters(M):
        x = int(ceil(log(pow(2, M + 1) - N, 2)))
        return pow(2, M + 1) * (M - x) + pow(2, x) + N * (x - 1)
    else:
        return 0

def max_num_characters(M):
    """This function returns maximal number of characters which could be encoded
    using unique binary sequences."""
    return pow(2, M + 1) - 2
