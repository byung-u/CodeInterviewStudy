#!/usr/bin/env python3
from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    list_N = input().split()
    K = int(input())
    c1, c2 = 0, 0
    for c in permutations(list_N, K):
        c1 += 1
        if 'a' in c:
            c2 += 1
    res = '%.4f' % (c2 / c1)
    print(res)
