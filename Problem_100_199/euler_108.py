#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 108
In the following equation x, y, and n are positive integers.

1x
 + 
1y
 = 
1n

For n = 4 there are exactly three distinct solutions:

15
 + 
120
 = 
14
16
 + 
112
 = 
14
18
 + 
18
 = 
14

What is the least value of n for which the number of distinct solutions exceeds one-thousand?
NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
'''


from itertools import count
def p110_distinct(n):
    L = n * 2
    cnt = 0
    for x in range(L, n, -1):
        if x - n <= 0:
            continue
        y = n * x / (x - n)
        if y.is_integer():
            cnt += 1
    return cnt

def p108():  # 180180 245.39s < runtime (too slow..)
    max_d = 0
    for k in count(1260, 20):
        d = p110_distinct(k)
        if max_d < d:
            max_d = d
            if max_d > 1000:
                print([k], d)
                return
    return


p108()
