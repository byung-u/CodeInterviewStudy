#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 211
For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,
σ2(10) = 1 + 4 + 25 + 100 = 130.
Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.
'''
from functools import reduce
from math import sqrt
from util import is_square

def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(n - 2, n - 1, n) == 1


def prime_factors(n):
    i = 2
    factors = {}
    while n % 2 == 0:
        n //= 2
        factors[2] = factors.get(2, 0) + 1

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors


# https://en.wikipedia.org/wiki/Divisor_function#Properties
def sigma_x(n, x):
    pf = prime_factors(n)
    s = 1
    for p, a in pf.items():
        s *= ((p ** ((a + 1) * x) - 1) / (p ** x - 1))
    return int(s)

def p211_6hour():
    total = 0
    for n in range(1, 64000000):
        if is_prime(n):
            continue
        ds = sigma_x(n, 2)  # divisor square sum
        if is_square(ds):
            total += n
            print('[perfect]', [n], ds)
    print(total)
    return


def p211():
    maxN = 64000000
    f = [0] * maxN
    for i in range(1, maxN):
        for j in range(1, maxN):
            if j * i >= maxN:
                break
            f[i * j] += i * i
    ans = 0
    for i in range(0, maxN):
        if is_square(f[i]):
            ans += i
    print(ans)


p211()
