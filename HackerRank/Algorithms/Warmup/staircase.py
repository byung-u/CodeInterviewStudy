#!/usr/bin/env python3

n = 6
space = ' '
sharp = '#'
for i in range(n - 1, -1, -1):
    print(space * i + sharp * (n - i))
