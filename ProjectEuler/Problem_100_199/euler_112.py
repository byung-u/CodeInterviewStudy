#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import count
'''
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

def is_bouncy(n):  # dreamshire
    inc, dec, s = False, False, str(n)
    for i in range(len(s)-1):
        if s[i+1] > s[i]:
            inc = True
        elif s[i+1] < s[i]:
            dec = True
        if inc and dec:
            return True
    return False

def is_bouncy_slow(n):
    POSITIVE = 1
    NEGATIVE = 2
    last_flag = 0
    sn = list(map(int, str(n)))
    for i in range(1, len(sn)):
        diff = sn[i] - sn[i-1]
        if diff < 0:
            flag = NEGATIVE
        elif diff > 0:
            flag = POSITIVE
        else:
            flag = last_flag

        if last_flag != flag and last_flag != 0:  # bouncy
            return True
        last_flag = flag

    return False


def p112():  # 6sec < runtime
    bouncy = 0
    for i in count(1):
        if is_bouncy(i):
            bouncy += 1
        r = bouncy * 100 / i
        if r == 99:
            print('[112]: ', i)
            break
p112()
