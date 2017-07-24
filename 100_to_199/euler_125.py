#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 125
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164.
Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
'''


from util import is_palindromic


def p125():
    # Answer: 2906969179, 0.29s
    result = set()
    double = [i ** 2 for i in range(1, 10001)]
    ld = len(double)
    for i in range(0, ld):
        s = double[i]
        for j in range(i + 1, ld):
            s += double[j]
            if s > 100000000:
                break
            if is_palindromic(str(s)):
                result.add(s)
    print(sum(result))
    return


p125()
