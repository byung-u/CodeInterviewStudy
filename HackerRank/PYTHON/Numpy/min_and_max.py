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
print(numpy.max(numpy.min(n, axis=1)))
