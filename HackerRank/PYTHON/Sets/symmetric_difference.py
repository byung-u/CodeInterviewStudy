#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    M = int(input())
    lm = input().split()
    N = int(input())
    ln = input().split()
    sm = set(lm)
    sn = set(ln)
    res = set()
    res.update(sm.difference(sn))
    res.update(sn.difference(sm))
    res = sorted(list(map(int, res)))
    for r in res:
        print(r)
