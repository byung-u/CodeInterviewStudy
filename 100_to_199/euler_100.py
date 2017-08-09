#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
'''

from itertools import count
from math import sqrt, ceil


# https://oeis.org/A001542
def get_nominator(n):
    a = ceil((((3 + 2 * sqrt(2)) ** n) - ((3 - 2 * sqrt(2)) ** n)) / (2 * sqrt(2)))
    return a


def p100_use_diophantine():
    L, x, y = 10 ** 12, 1, 1
    while y < L: x, y = 3 * x + 2 * y - 2, 4 * x + 3 * y - 3
    print(x)


# Actually Diophantine pairs.. https://oeis.org/A011900
def p100():  # Answer: 756872327473, 0.01s
    L = 10 ** 12
    n = 1
    for i in count(1):
        np =  get_nominator(i // 2)  # pattern is repeated
        res = n * (n+np)
        n = n + np
        if res * 1.414 > L:  # 15/21, 85/120 is around 1.414xxxx
            print(res)
            break
    return


p100()
