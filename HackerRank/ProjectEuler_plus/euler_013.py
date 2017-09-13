#!/usr/bin/env python3

t = int(input())
digit = []
for a0 in range(t):
    digit.append(int(input()))
print(str(sum(digit))[:10])
