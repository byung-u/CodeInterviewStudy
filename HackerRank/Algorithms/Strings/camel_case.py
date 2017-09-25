#!/usr/bin/env python3
import sys

S = input().strip()
print(len([s for s in S[1:] if s.isupper()]) + 1)
