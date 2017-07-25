#!/usr/bin/env python3
import operator

from math import sqrt
from functools import reduce

#    p ∣ a  (a divides b)
#    p ∤ a  (a does not divides b)

# 확장 유클리드 호제법을 이용한 부정방적식의 해 구하기
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# ax + by = g = gcd(a, b).
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0  # gcd, x, y


# 일차 합동식
# http://nicklib.com/library/algo/c/congruence_t.html
# a*x ≡ b (mod m)일 때, x의 값을 구함.
def congruence(a, b, m):
    c, d, e, f = a, m, b, 0
    q, r, tmp = 0, c % d, 0
    while r != 0:
        q, c, d, tmp = c // d, d, r, f
        f, e, r = e - (q * f), tmp, c % d
    if b % d != 0:
        return -1
    q = (f // d) % (m // d)
    if q < 0:
        q += m // d
    return q
