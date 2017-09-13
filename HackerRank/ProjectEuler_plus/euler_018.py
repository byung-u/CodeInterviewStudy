#!/usr/bin/env python3

t = int(input())
for i in range(t):
    n = int(input())
    tri = []
    for j in range(n):
         tri.append(list(map(int, input().split())))
    rtri = [tri[i] for i in reversed(range(0, len(tri)))]
    len_tri = len(rtri) - 1
    for i in range(0, len_tri):
        for j in range(0, len_tri - i):
            rtri[i + 1][j] = max(rtri[i][j] + rtri[i + 1][j], rtri[i][j + 1] + rtri[i + 1][j])
    print(rtri[n-1][0])
