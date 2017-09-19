#!/usr/bin/env python3
import numpy


arr = list(map(int, input().strip().split(' ')))
print(numpy.reshape(arr, (3, 3)))
