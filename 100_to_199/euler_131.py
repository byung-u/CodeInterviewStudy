#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 131
There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.
For example, when p = 19, 83 + 82×19 = 123.
What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.
How many primes below one million have this remarkable property?
'''


from util import prime_sieve
from itertools import count


def is_perfect_cube(x):
    # x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x


def p131():  # Answer: 173, 68.54s  Mac pro 2016
    cnt = 0
    primes = prime_sieve(1000000)
    for p in primes:
        for i in count(1):
            n = i ** 3
            if is_perfect_cube(n + p):
                if is_perfect_cube(n ** 2):
                    # print('[great] ', [p, n, i], n**2, n+p)
                    cnt += 1
                    break
            if i > 600:
                break
    print(cnt)


p131()
