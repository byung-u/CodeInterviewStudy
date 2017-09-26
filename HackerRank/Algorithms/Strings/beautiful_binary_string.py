#!/usr/bin/env python3

import sys
import re
from itertools import combinations

def minSteps(n, B):
    b = re.findall('010', B)
    return len(b)

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)

