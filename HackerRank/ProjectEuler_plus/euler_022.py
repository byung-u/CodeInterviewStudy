#!/usr/bin/env python3
import sys
from collections import OrderedDict

def get_name_worth(d, aa):
    worth = 0
    for i in range(len(aa)):
        worth += d[aa[i]]
    return worth


position_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
t = int(input())
d = {}

for i in range(t):
    name = input()
    d[name] = 0

od = OrderedDict(sorted(d.items()))
for idx, (name, val) in enumerate(od.items()):
    worth = get_name_worth(position_dict, name)
    worth = ((idx + 1) * worth)
    od[name] = worth

t = int(input())
for i in range(t):
    name = input()
    print(od[name])
