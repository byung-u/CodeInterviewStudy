#!/usr/bin/env python3
from itertools import combinations_with_replacement

if __name__ == '__main__':
    k = input().split()
    S, n = k[0], int(k[1])
    res = [''.join(p) for p in combinations_with_replacement(S, n)]
    for i, t in enumerate(res):
        res[i] = ''.join(sorted(t))
    print('\n'.join(sorted(res)))

