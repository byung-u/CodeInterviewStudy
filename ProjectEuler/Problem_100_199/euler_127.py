#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util import prime_factors_uniq, prime_sieve
from functools import reduce

'''
Problem 127
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:
GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.
Find ∑c for c < 120000.
'''


def rad(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return reduce(lambda x, y: x * y, list(prime_factors_uniq(n)))


def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(n - 2, n - 1, n) == 1


def prime_factors(n, primes):
    factors = set()
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            while n % p == 0:
                n //= p
                factors.add(p)
            if is_prime(n):
                factors.add(n)
                return factors
    return factors


def p127_check(a, b, c, primes):
    r = []
    r.extend(prime_factors(a, primes))
    r.extend(prime_factors(b, primes))
    r.extend(prime_factors(c, primes))

    if len(r) != len(set(r)):
        return False

    return True


def p127():  # Answer 18407904, 17 min....Orz
    sum_c = 0
    L = 120000
    primes = prime_sieve(L)
    lrad = [0] * L
    for a in range(1, L // 2):
        if lrad[a] == 0:
            lrad[a] = rad(a)
        if a % 2 == 0:
            inc = 2
        else:
            inc = 1
        for b in range(a + 1, L - 1, inc):
            if lrad[b] == 0:
                lrad[b] = rad(b)
            c = a + b
            if c >= L:
                break
            if lrad[c] == 0:
                lrad[c] = rad(c)
            if (lrad[a] * lrad[b] * lrad[c]) >= c:
                continue
            if p127_check(a, b, c, primes):
                print(a, b, c)
                sum_c += c

    print(sum_c)
    return


p127()
