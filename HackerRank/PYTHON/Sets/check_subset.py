#!/usr/bin/env python3

import sys

for _ in range(int(input())):
    An, A = int(input()), set(map(int, input().split()))
    Bn, B = int(input()), set(map(int, input().split()))
    print(A.issubset(B))
