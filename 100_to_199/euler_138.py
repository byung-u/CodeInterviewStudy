#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem 138
Consider the isosceles triangle with base length, b = 16, and legs, L = 17.


By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(172 − 82) = 15, which is one less than the base length.
With b = 272 and L = 305, we get h = 273, which is one more than the base length, and this is the second smallest isosceles triangle with the property that h = b ± 1.
Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.
'''
from itertools import count
from decimal import Decimal
from math import modf


# Pythagorean approximations
# http://oeis.org/A195615 (FORMULA)
def a(n):
    if n == 0:
        return 15
    if n == 1:
        return 273
    if n == 2:
        return 4895
    return 17 * a(n - 1) + 17 * a(n - 2) - a(n - 3)


def p138():
    highs = [a(i) for i in range(0, 12)]
    result = []
    for h in highs:
        hd = h ** 2
        bd = ((h - 1) // 2) ** 2
        ret = Decimal(hd + bd).sqrt()
        ret_float, ret_int = modf(ret)
        if ret_float == 0.0:
            # print('[-]', [h], ret, ret_float, ret_int)
            result.append(int(ret_int))
            continue
        bd = ((h + 1) // 2) ** 2
        ret = Decimal(hd + bd).sqrt()
        ret_float, ret_int = modf(ret)
        if ret_float == 0.0:
            # print('[+]', [h], ret, ret_float, ret_int)
            result.append(int(ret_int))
    print(sum(result))


'''
@youth4ever solution
Using the Pythagorean Triplets and remarking that if we use :
h = m**2-n**2
b = 2*m*n
L = m**2 + n**2
we can start with (m,n) = (4,1) next sequence will be :
(m,n)= (17, 4), then (m,n)= (72, 17), (m,n)=(305, 72)... and so on.

Therefore the pattern becomes obvious. I will not insist on that. Here is the solution, about 10 ms in Python3 :

'''
def special_Isosceles_Tiangles(how_many) :
    cnt, S = 0, 0
    m, n = 4, 1
    while True :
        for m in count(m, 1):
            h = m ** 2 - n ** 2
            b = 2 * m * n
            L = m ** 2 + n ** 2
            if b * 2 == h + 1 or b * 2== h - 1:
                cnt += 1
                print('(m,n)=' ,m,n,'        (h, b, L)= ', (h, b ,L) )
                S += L
                break
        n = m
        m = int(4.236 * n)
        if cnt == how_many :
            return print('\nAnswer :', S)

special_Isosceles_Tiangles(12)
# p138()
