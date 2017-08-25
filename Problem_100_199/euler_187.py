#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 187
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors:
4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
'''

from util import prime_sieve


def p187():
    cnt = 0
    primes = prime_sieve(49999992)
    lp = len(primes)
    for i in range(0, lp - 1):
        for j in range(i, lp):
            if primes[i] * primes[j] > 100000000:
                break
            # print(primes[i]* primes[j], '\t', primes[i], primes[j])
            cnt += 1
    print(cnt)
    return


p187()
