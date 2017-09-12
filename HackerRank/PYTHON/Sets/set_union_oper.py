#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    i = int(input())
    A = set(map(int, input().split()))
    j = int(input())
    B = set(map(int, input().split()))
    res = A.union(B)
    print(len(res))
