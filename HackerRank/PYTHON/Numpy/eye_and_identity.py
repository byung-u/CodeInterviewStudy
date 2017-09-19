#!/usr/bin/env python3
import sys
import numpy

s = list(map(int, input().strip().split(' ')))
print(numpy.eye(s[0], s[1]))
