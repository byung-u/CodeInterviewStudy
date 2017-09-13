#!/usr/bin/env python3
from itertools import permutations

if __name__ == '__main__':
    k = input().split()
    S, n = k[0], int(k[1])
    res = [''.join(p) for p in permutations(S, n)]
    print('\n'.join(sorted(res)))

