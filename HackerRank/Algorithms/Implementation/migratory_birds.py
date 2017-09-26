#!/usr/bin/env python3

import sys
from itertools import product

def divisibleSumPairs(n, k, ar):
    # return len([p for p in product(ar, repeat=2) if p[0] < p[1] and (p[0] + p[1]) >= k and (p[0] + p[1]) % k == 0])
    return len([i for i in range(0, n) for j in range(i + 1, n) if (ar[i] + ar[j]) % k == 0])



n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
