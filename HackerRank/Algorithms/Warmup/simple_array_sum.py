#!/usr/bin/env python3

import sys
from functools import reduce

def simpleArraySum(n, ar):
    return reduce(lambda x, y: x + y, ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
