#!/usr/bin/env python3
import sys

S = input().strip()
cnt = 0 
for s in S[0::3]:
    if s != 'S':
        cnt += 1
for s in S[1::3]:
    if s != 'O':
        cnt += 1
for s in S[2::3]:
    if s != 'S':
        cnt += 1
print(cnt)
