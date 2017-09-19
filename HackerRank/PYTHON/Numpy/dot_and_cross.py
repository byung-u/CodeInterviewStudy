#!/usr/bin/env python3
import sys
import numpy

N = int(input())
arr = []
for _ in range(0, N):
    temp = list(map(int, input().split()))
    arr.append(temp)
n = numpy.array(arr)

arr = []
for _ in range(0, N):
    temp = list(map(int, input().split()))
    arr.append(temp)
m = numpy.array(arr)
print(numpy.dot(n, m))
