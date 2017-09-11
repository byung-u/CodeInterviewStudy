#!/usr/bin/env python3
import sys
from collections import defaultdict


if __name__ == '__main__':
    I =  input().split()
    n, m = int(I[0]), int(I[1])
    d = defaultdict(list)
    for _ in range(n):
        d[n].append(input())
    for _ in range(m):
        d[m].append(input())

    if n == 1 and m == 1:
        if d[n][0] == d[m][1]:
            print(1)
        else:
            print(-1)
    else:
        for dm in d[m]:
            res = ""
            for idx, dn in enumerate(d[n]):
                if dm == dn:
                    res += '%d ' % (idx + 1)
            else:
                if len(res) == 0:
                    print(-1)
                else:
                    print(res)
