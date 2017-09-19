#!/usr/bin/env python3
import sys
import numpy

s = tuple(map(int, input().strip().split(' ')))
print(numpy.zeros(s, dtype=int))
print(numpy.ones(s, dtype=int))
