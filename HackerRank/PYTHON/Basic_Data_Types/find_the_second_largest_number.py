#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    n = int(input())
    L = sorted(list(set(map(int, input().split()))))
    print(L[-2])

