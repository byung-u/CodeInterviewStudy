#!/usr/bin/env python3
import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = list(reversed([int(h1_temp) for h1_temp in input().strip().split(' ')]))
h2 = list(reversed([int(h2_temp) for h2_temp in input().strip().split(' ')]))
h3 = list(reversed([int(h3_temp) for h3_temp in input().strip().split(' ')]))

while True:
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    min_val = min([s1, s2, s3])
    if s1 == s2 == s3:
        print(s1)
        break
    if s1 > min_val:
        sum_h1 = s1
        while sum_h1 > min_val:
            sum_h1 -= h1[-1]
            h1.pop()
    elif s2 > min_val:
        sum_h2 = s2
        while sum_h2 > min_val:
            sum_h2 -= h2[-1]
            h2.pop()
    elif s3 > min_val:
        sum_h3 = s3
        while sum_h3 > min_val:
            sum_h3 -= h3[-1]
            h3.pop()
