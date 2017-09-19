#!/usr/bin/env python3

import sys

A = set(map(int, input().split()))
for _ in range(int(input())):
    N = set(map(int, input().split()))
    if not A.issuperset(N):
        print('False')
        sys.exit(1)
print('True')
