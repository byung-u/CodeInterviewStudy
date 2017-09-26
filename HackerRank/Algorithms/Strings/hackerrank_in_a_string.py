#!/usr/bin/env python3
import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    start = s.find('h', 0)
    if start == -1:
        print('NO')
        continue
    start = s.find('a', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('c', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('k', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('e', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('r', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('r', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('a', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('n', start+1)
    if start == -1:
        print('NO')
        continue
    start = s.find('k', start+1)
    if start == -1:
        print('NO')
        continue
    print('YES')
