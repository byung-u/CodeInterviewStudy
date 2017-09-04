#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 132
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.
For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.
Find the sum of the first forty prime factors of R(10^9).
'''
from util import prime_sieve
from algorithms import modular_pow
from itertools import islice


'''
1.  ((10 ** n) - 1) / 9 = Repunit
    ((10 ** n) - 1) / 9 = R * Primes
    (10 ** n) - 1       = R * Primes * 9
    (10 ** n)           = (R * Primes * 9) + 1
    ------------------------------------------
    (10 ** n) ≡ 1 (mod 9 * Primes)

    So we can use
         if pow(10, n, 9 * primes) == 1:
             print('got it')  # but it's too slow for (10 ** (10 ** 9))

    As a result we use Right to left binary method one of modular exponentiation.
         if modular_pow(base, exponent , modulus) == 1:
             print('got it')
'''
def p132():
    primes = prime_sieve(10 ** 6)
    base = 10
    exp = 10 ** 9
    cnt = 0
    s = 0
    for p in primes:
        if modular_pow(base, exp, 9 * p) == 1:
            s += p
            cnt += 1
            if cnt == 40:
                break
    print(s)


def p132_nice():
    primes = prime_sieve(10 ** 6)
    base = 10
    exp = 10 ** 9
    result = sum(islice((p for p in primes if modular_pow(base, exp, 9 * p) == 1), 0, 40))
    print("The result is:", result)



p132()
