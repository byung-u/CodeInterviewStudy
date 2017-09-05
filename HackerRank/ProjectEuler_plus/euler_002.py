#!/usr/bin/env python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i1, i2, res = 1, 1, 0
    while True:
        i1, i2 = i2, i1 + i2
        if i2 >= n + 1:
            break
        if i2 % 2 == 0:
            res += i2
    print(res)

