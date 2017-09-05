#!/usr/bin/env python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(reversed(list(map(int, input().strip().split(' ')))))
    b = list(reversed(list(map(int, input().strip().split(' ')))))
    cnt = 0
    total = 0
    while True:
        if total > x:
            break
        if len(a) == 0 or len(b) == 0:
            # print('what the')
            break
        if a[-1] > b[-1]:
            total += a[-1]
            # print('a', a[-1])
            a.pop()
            cnt += 1
        elif a[-1] < b[-1]:
            total += b[-1]
            # print('b', b[-1])
            b.pop()
            cnt += 1
        else:
            total += a[-1]
            # print('a', a[-1])
            a.pop()
            cnt += 1
    print(cnt)
