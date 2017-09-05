#!/usr/bin/env python3
import sys


def shift(input_list, n):
    n = n % len(input_list)
    return input_list[n:] + input_list[:n]


def is_palindromic(n):
    return n == n[::-1]

N = int(input())
S = list(input())

for i in range(N):
    res = shift(S, i)
    max_len = 0
    for j in range(N):
        temp_char = res[j]
        for k in range(j + 1, N):
            if i == 7:
                print([i], max_len, k, j)
            # if k - j + 2 <= max_len:
            #     break
            if temp_char == res[k] and is_palindromic(res[j:k+1]) and max_len < (k - j + 1):
                max_len = k - j + 1
    print(max_len)

# 12
# eededdeedede
# 5
# 7
# 7
# 7
# 7
# 9
# 9
# 9
# 9
# 7
# 5
# 4
