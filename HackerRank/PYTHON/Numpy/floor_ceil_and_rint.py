#!/usr/bin/env python3
import sys
import numpy

na = numpy.array(list(map(float, input().split())))
print(numpy.floor(na))
print(numpy.ceil(na))
print(numpy.rint(na))
