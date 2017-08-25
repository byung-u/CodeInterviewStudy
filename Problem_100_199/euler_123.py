#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 123
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.
For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.
The least value of n for which the remainder first exceeds 10^9 is 7037.
Find the least value of n for which the remainder first exceeds 10^10.
'''

from util import prime_sieve
'''
    ((pn - 1) ^ n + (pn + 1) ^ n) % (p[n] * p[n])
    ->       (2 * (n + 1) * p[n]) % (p[n] * p[n])

    (2 * (n + 1) * p[n]) % (p[n] * p[n]) will be equal to 2 when n + 1 is even
    and will be equal to (2 * (n + 1) * p[n]) when n + 1 is odd.
    Hence can reduce.
    ->       (2 * (n + 1) * p[n])
'''


def p123_nice():
    primes = prime_sieve(1000000)
    for n in range(7038, len(primes), 2):
        print([n], 2 * (n + 1) * primes[n])
        if 2 * (n + 1) * primes[n] > pow(10, 10):
            print(n + 1)
            break


def p123():  # Answer 21035
    primes = prime_sieve(1000000)
    for i in range(7038, len(primes), 2):
        n = i + 1
        p = primes[i]
        s = (p - 1) ** n + (p + 1) ** n
        p2 = p ** 2
        r = s % p2
        print([n], r)
        if len(str(r)) > 10:
            print(n)
            break
    return


p123_nice()
