#!/usr/bin/env python3

import sys
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n), int(k)]
    num = input().strip()
    print(max([reduce(lambda x, y: x * y, list(map(int, num[i:i + k]))) for i in range(0, n - k)]))
