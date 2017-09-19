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

arr = []
for _ in range(0, N):
    temp = list(map(int, input().split()))
    arr.append(temp)
m = numpy.array(arr)

print(numpy.add(n, m))
print(numpy.subtract(n, m))
print(numpy.multiply(n, m))
print(numpy.floor_divide(n, m))
print(numpy.mod(n, m))
print(numpy.power(n, m))
