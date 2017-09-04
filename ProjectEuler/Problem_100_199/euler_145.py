#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 145
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).
There are 120 reversible numbers below one-thousand.
How many reversible numbers are there below one-billion (109)?
'''


def is_all_odd(sum_n):
    for s in str(sum_n):
        if not int(s) & 1:
            return False
    return True


def is_reversible(n):
    if n % 10 == 0:
        return False
    str_n = str(n)
    if int(str_n[0]) % 2 == int(str_n[-1]) % 2:
        return False
    sum_n = n + int(str_n[::-1])
    return is_all_odd(sum_n)


def p145():
    # ret = [i for i in range(1, 1000000000) if is_reversible(i)]
    r = 0
    i = 1
    while i != 1000000000:
        if is_reversible(i):
            r += 1
        i += 1
    print('[145]: ', r)


p145()


''' 
[I think this solution is BEST]
Instead, I did this one with pencil and paper
on my coffee break.

(1) There are no 1-digit solutions.

(2) For ab to be a two-digit solution, 
    a+b must be odd and less than 10, with neither a nor b zero. 
    There are 20 pairs.

(3) For abc to be a three-digit solution, 
    a+c must be odd and greater than 10, 20 choices for ac, 
    2b must be less than 10.  Five choices for b, 
    20 * 50 = 100 solutions.

(4) For abcd to be a four-digit solution, 
    a+d must be odd and less than 10, neither a nor d can be zero, 20 choices for ad,
    b+c must be odd and less than 10.  30 for bc,
    600 solutions.

(5) There are no five-digit solutions.

(6) For abcdef to be a six-digit solution, 
    a+f, b+e, c+d must all be odd and less than 10. a and f cannot be zero.
    20 choices for af,
    30 for be,
    30 for cd,
    20 * 30 * 30 = 18000 solutions.

(7) For abcdefg to be a seven digit solution:
    a+g odd and greater than 10, 20 for ag,
    b+f even and greater than 10, 25 for bf,
    c+e odd and greater than 10, 20 for ce,
    2d less than 10, 5 choices for d,
    20 * 25 * 20 * 5 = 50000 solutions.

(8) Eight digit solutions are like 2-, 4-, 6-digit solutions.
    abcdefgh; a+h, b+g, c+f, d+e all odd and less than 10,
    neither a nor h can be zero. 
    20*30*30*30=540000 solutions

(9) There are no nine-digit solutions.

In general, moving forward, there are
    2n-digit    20 * 30^(n-1)
    4n+1-digit  no
    4n+3-digit  5 * 20**(n+1) * 25**n
'''

