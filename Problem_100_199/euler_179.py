#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
from util import is_prime

'''
Problem 179
Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''


def factor_cnt(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return len(results)


def p179():  # 60 min > run time  (bad..)
    L = 10 ** 7
    cnt = 1  # 2, 3
    last_fc = 0
    for i in range(2, L):
        if is_prime(i):
            last_fc = 0
            continue
        fc = factor_cnt(i)
        if last_fc == fc:
            cnt += 1
            print([i], fc, last_fc)
        last_fc = fc

    print('[179]: ', cnt)
    return

p179()
