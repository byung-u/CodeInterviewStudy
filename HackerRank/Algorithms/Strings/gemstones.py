#!/usr/bin/env python3
import sys

def gemstones(arr):
    s1 = set(arr[0])
    for i in range(1, len(arr)):
        s2 = set(arr[i])
        s1 = s1.intersection(s2)
    return len(s1)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)

