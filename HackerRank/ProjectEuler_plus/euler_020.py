#!/usr/bin/env python3
from math import factorial

t = int(input())
digit = []
for a0 in range(t):
    n = int(input())
    print(sum(map(int, (str(factorial(n))))))

