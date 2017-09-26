#!/usr/bin/env python3

t = int(input())
for i in range(t):
    n = int(input())
    print(sum(map(int, str(2 ** n))))
