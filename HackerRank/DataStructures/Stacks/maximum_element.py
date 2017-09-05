#!/usr/bin/env python3

t = int(input().strip())
elem = []
max_elem = 0
for a0 in range(t):
    n = input().split()
    if n[0] == '1':
        if max_elem < int(n[1]):
            max_elem = int(n[1])
        elem.append(int(n[1]))
    elif n[0] == '2':
        max_elem = 0
        elem.pop()
        if len(elem) > 0:
            max_elem = max(elem)
    else:  # 3
        print(max_elem)
