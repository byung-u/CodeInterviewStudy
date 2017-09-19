#!/usr/bin/env python3
import sys
import numpy

arr = []
for _ in range(int(input())):
    arr.append(list(map(float, input().split())))
n = numpy.array(arr)
print(numpy.linalg.det(n))
