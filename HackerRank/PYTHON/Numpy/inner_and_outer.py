#!/usr/bin/env python3
import sys
import numpy

n = numpy.array(list(map(int, input().split())))
m = numpy.array(list(map(int, input().split())))
print(numpy.inner(n, m))
print(numpy.outer(n, m))
