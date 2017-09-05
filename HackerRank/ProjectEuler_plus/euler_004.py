#!/usr/bin/env python3

import sys

def is_palindromic(n):
    return n == n[::-1]

results = set()
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        if is_palindromic(str(k)):
            results.add(k)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(n - 1, 1, -1):  # less than N
        if i in results:
            print(i)
            break
