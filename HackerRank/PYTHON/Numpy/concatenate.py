#!/usr/bin/env python3
import numpy

n, m = [], []
arr = list(map(int, input().strip().split(' ')))
N, M, P = arr[0], arr[1], arr[2]
for _ in range(N):
    arr = list(map(int, input().strip().split(' ')))
    n.append(arr)
for _ in range(M):
    arr = list(map(int, input().strip().split(' ')))
    m.append(arr)

na = numpy.array(n)
ma = numpy.array(m)
a = numpy.concatenate((na, ma), axis=0)
print(a)
