#!/usr/bin/env python3

import sys
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(6)
    else:
        nums = [2, 3]
        for i in range(4, n + 1):
            for n in nums:
                if i % n == 0:
                    i //= n
            nums.append(i)
        print(reduce(lambda x, y: x * y, nums))
