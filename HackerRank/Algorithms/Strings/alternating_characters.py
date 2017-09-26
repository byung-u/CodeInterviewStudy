#!/usr/bin/env python3
import sys
from itertools import groupby

# Success

def alternatingCharacters(s):
    CS = ([list(g) for k, g in groupby(s)])
    cnt = 0
    for C in CS:
        cnt += len(C) - 1
    return cnt
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)

