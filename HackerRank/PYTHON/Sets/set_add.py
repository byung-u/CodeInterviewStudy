#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    N = int(input())
    res = set()
    for _ in range(N):
        res.add(input())
    print(len(res))
