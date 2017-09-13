#!/usr/bin/env python3
from itertools import combinations

if __name__ == '__main__':
    k = input().split()
    S, n = k[0], int(k[1])
    res = []
    for i in range(1, n + 1):
        temp = [''.join(p) for p in combinations(S, i)]
        if i > 1:
            for i, t in enumerate(temp):
                temp[i] = ''.join(sorted(t))
        res.extend(temp)
    res.sort()
    res.sort(key=len, reverse=False)
    print('\n'.join(res))

