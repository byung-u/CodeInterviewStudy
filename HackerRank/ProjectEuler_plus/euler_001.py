#!/usr/bin/env python3

import sys


t = int(input().strip())
nums = []
for a0 in range(t):
    n = int(input().strip())
    nums.append(n)

for n in nums:
    n1 = (n - 1) // 3
    n2 = (n - 1) // 5
    n3 = (n - 1) // 15
    r1 = 3 * (n1 * (n1 + 1) // 2)
    r2 = 5 * (n2 * (n2 + 1) // 2)
    r3 = 15 * (n3 * (n3 + 1) // 2)
    print(r1 + r2 - r3)
