#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        req = input().split()
        if req[0] == 'pop':
            if len(s) != 0:
                s.pop()
        if req[0] == 'remove':
            try:
                s.remove(int(req[1]))
            except:
                pass
        if req[0] == 'discard':
            s.discard(int(req[1]))

    print(sum(s))

