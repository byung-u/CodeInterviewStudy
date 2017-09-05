#!/usr/bin/env python3


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for a in (arr[::-1]):
    print(a, end=" ")
print()

