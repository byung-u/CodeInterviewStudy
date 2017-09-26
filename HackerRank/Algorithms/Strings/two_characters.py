#!/usr/bin/env python3

import sys
from itertools import combinations

s_len = int(input().strip())
S = input()
set_s = set(S)
max_len = 0
for p in combinations(set_s, 2):
    temp = [s for s in S if p[0] == s or p[1] == s]
    if len(set(temp[0::2])) == 1 and len(set(temp[1::2])) == 1:
        if max_len < len(temp):
            max_len = len(temp)
print(max_len)
sys.exit(1)
