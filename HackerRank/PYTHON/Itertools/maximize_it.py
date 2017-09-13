#!/usr/bin/env python3
import sys
from itertools import combinations, product
from functools import reduce

if __name__ == '__main__':
    temp = input().split()
    K = int(temp[0])
    M = int(temp[1])
    val = []
    for _ in range(K):
        temp = (list(map(int, input().split()))[1:])
        l = [v ** 2 for v in temp]
        val.append(l)
     
    max_sum = 0
    for p in product(*val):
        s = reduce(lambda x, y: x + y, p) % M
        if s == M - 1:
            print(s)
            sys.exit(1)

        if max_sum < s:
            max_sum = s
    print(max_sum)
