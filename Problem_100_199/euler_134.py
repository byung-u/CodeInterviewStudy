#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 134
Consider the consecutive primes p1 = 19 and p2 = 23.
It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.
In fact, with the exception of p1 = 2 and p2 = 5,
for every pair of consecutive primes, p2 > p1,
there exist values of n for which the last digits are formed by p1 and n is divisible by p2.
Let S be the smallest of these values of n.
Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
'''

from util import prime_sieve

# a*x ≡ b (mod m), x ?
def congruence(a, b, m):
    c, d, e, f = a, m, b, 0
    q, r, tmp = 0, c % d, 0
    while r != 0:
        q, c, d, tmp = c // d, d, r, f
        f, e, r = e - (q * f), tmp, c % d
    if b % d != 0:
        return -1
    q = (f // d) % (m // d)
    if q < 0:
        q += m // d
    return q 


def p134():  # 18613426663617118, 2sec < run time
    total = 0
    L = 1000000
    primes = prime_sieve(L + 50)
    for i in range(2, len(primes) - 1):
        p1 = primes[i]
        if p1 >= L:
            break
        p2 = primes[i + 1]
        k = 1
        while k < p1:
            k *= 10
        small_n = congruence(p2, p1, k)
        total += (small_n * p2)
    print(total)


p134()
