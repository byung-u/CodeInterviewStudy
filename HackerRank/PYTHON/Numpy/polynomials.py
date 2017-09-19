#!/usr/bin/env python3
import sys
import numpy

n = numpy.array(list(map(float, input().split())))
x = int(input())

print(numpy.polyval(n, x))
