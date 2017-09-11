#!/usr/bin/env python3
import sys
from collections import namedtuple

if __name__ == '__main__':
    N = int(input())
    category =  input().split()
    for i, c in enumerate(category):
        if c == 'MARKS':
            idx_marks = i
    # print('->>>', idx_marks)
    infos = []
    for _ in range(N):
        info = input().split()
        infos.append(int(info[idx_marks]))
    res = '%.2f' % (sum(infos) / len(infos))
    print(res)
