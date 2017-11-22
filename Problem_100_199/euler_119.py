#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 119
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.
We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
You are given that a2 = 512 and a10 = 614656.
Find a30.
'''


'''
I used unix command

    % ./euler_119.py | sort -k 3 -n | head -n 30 | tail -n 1 | awk '{print $2 ** $3}'
    248155780267521

    answer is 248155780267521
'''


def p119():
    idx = 0
    for i in range(2, 100):
        for j in range(2, 100):
            k = i ** j
            if i == sum(list(map(int, str(k)))):
                idx += 1
                print(idx, i, j)
    return


p119()
