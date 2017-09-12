#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    H = (input().split())
    A = set(input().split())
    B = set(input().split())
    res = 0
    for h in H:
        if h in A:
            res += 1
        if h in B:
            res -= 1
    print(res)
