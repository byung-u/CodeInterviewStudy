#!/usr/bin/env python3
import sys
import numpy

s = list(map(int, input().split()))
N, M = s[0], s[1]
arr = []
for _ in range(0, N):
    temp = list(map(int, input().split()))
    arr.append(temp)
n = numpy.array(arr)
print(numpy.mean(n, axis=1))
print(numpy.var(n, axis=0))
print(numpy.std(n, axis=None))
