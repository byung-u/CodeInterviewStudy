#!/usr/bin/env python3
import numpy

n = []
arr = list(map(int, input().strip().split(' ')))
N = arr[0]
M = arr[1]
for _ in range(N):
    arr = list(map(int, input().strip().split(' ')))
    n.append(arr)

na = numpy.array(n)
print(numpy.transpose(na))
print(na.flatten())
