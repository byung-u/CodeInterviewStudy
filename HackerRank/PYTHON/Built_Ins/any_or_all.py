#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    N = int(input())
    n = input().split()
    print(all(int(i) > 0 for i in n) and any(j == j[::-1] for j in n))
