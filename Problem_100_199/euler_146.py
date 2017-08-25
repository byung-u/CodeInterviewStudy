#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 146
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.
What is the sum of all such integers n below 150 million?
'''


# https://en.wikipedia.org/wiki/Fermat_primality_test#Concept
# https://gist.github.com/bnlucas/5857437
# a ^ (n-1) ≡ 1 (mod n)
def is_prime_fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    # Pick a randomly in the range [2, n − 2]
    # use 2
    return pow(n - 2, n - 1, n) == 1  # 2 ^ (n - 1) ≡ 1 (mod n)


def is_prime_pattern(n):
    if ( pow(2, (n + 1) - 1, n + 1) != 1 or
         pow(2, (n + 3) - 1, n + 3) != 1 or
         pow(2, (n + 7) - 1, n + 7) != 1 or
         pow(2, (n + 9) - 1, n + 9) != 1 or
         pow(2, (n + 13) - 1, n + 13) != 1 or
         pow(2, (n + 27) - 1, n + 27) != 1):
        return False

    # consecutive prime check
    if is_prime_fermat(n + 11):
        return False
    for i in range(n + 15, n + 27, 2):
        if is_prime_fermat(i):
            return False
    return True


# python3 euler_146.py  98.05s user 0.38s system 99% cpu 1:38.95 total
# sum= 676333270
def p146():
    pp = []
    for n in range(10, 150000000, 10):
        if n % 3 == 0 or n % 7 == 0 or n % 13 == 0:
            continue
        if is_prime_pattern(n ** 2):
            pp.append(n)
    print('sum=', sum(pp))
    return


p146()
