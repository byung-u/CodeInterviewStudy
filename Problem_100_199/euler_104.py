#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 104
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits,
is the first Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order).
And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''


def is_pandigital(n, s=9):
    return len(n) == s and not '123456789'[:s].strip(n)


def p104():
    n1, n2, F = 1, 1, 3
    while (1):
        n = n1 + n2
        # if is_pandigital(str(n)[:9]) and is_pandigital(str(n)[-9:]):
        #     break
        if is_pandigital(str(n % 1000000000)):
            # print('[last 9]', F, str(n)[-9:])
            if is_pandigital(str(n)[:9]):
                print('[104]: ', F, str(n)[:9])
                break
        n1, n2 = n2, n
        F += 1


p104()
