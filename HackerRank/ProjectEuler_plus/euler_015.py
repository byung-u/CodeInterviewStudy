#!/usr/bin/env python3
from math import factorial

MAX_NUM = (10 ** 9) + 7
t = int(input())
for i in range(t):
    n = input().split()
    N, M = int(n[0]), int(n[1])
    print((factorial(M + N) // (factorial(M) * factorial(N))) % MAX_NUM)
