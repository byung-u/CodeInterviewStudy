#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 200
We shall define a sqube to be a number of the form, p2q3, where p and q are distinct primes.
For example, 200 = 5^2*2^3 or 120072949 = 23^2*61^3.
The first five squbes are 72, 108, 200, 392, and 500.
Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.
Find the 200th prime-proof sqube containing the contiguous sub-string "200".
'''

from functools import reduce
from util import prime_sieve, is_prime
def p2q3(p, q):
    return (p ** 2) * (q ** 3)

def prime_proof(str_n):
    l = len(str_n)

    for i in range(l):
        ln = list(map(int, str_n))
        ln[i] = 0
        c = int(reduce(lambda x, y:str(x) + str(y), ln))
        # print(c, l - i - 1)
        for j in range(10):
            r = c + j * 10 ** (l - i - 1)
            if is_prime(r):
                return False
            # print('\t', r)
    return True


def p200_slow():
    res = []
    primes = prime_sieve(400000)
    for p1 in primes:
        for p2 in primes:
            if p1 == p2:
                continue
            sqube = p2q3(p1, p2)
            if sqube > 7999728002312:
                break
            str_sqube = str(sqube)
            if str_sqube.find('200') >= 0:
                if prime_proof(str_sqube):
                    print(p1, p2, sqube)
                    res.append(sqube)

    res = sorted(res)
    print(res[199])
    return

def p200():  # 229161792008, 6.12sec
    res = []
    primes = prime_sieve(200000)
    for p1 in primes:
        for p2 in primes:
            if p1 == p2:
                continue
            sqube = p2q3(p1, p2)
            if sqube > 7999728002312:
                break
            if sqube % 2 != 0 and sqube % 5 != 0:
                continue
            str_sqube = str(sqube)
            if str_sqube.find('200') >= 0:
                if prime_proof(str_sqube):
                    print(p1, p2, sqube)
                    res.append(sqube)

    res = sorted(res)
    print(res[199])
    return


p200()
