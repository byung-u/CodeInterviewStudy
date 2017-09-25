#!/usr/bin/env python3
import sys

def super_reduced_string(s):
    # Complete this function
    input_s = list(s)
    while len(input_s) > 1:
        for i in range(len(input_s) -1):
            try:
                if input_s[i] == input_s[i + 1]:
                    input_s.pop(i)
                    input_s.pop(i)
            except:
                if len(input_s) > 1:
                    break
        else:
            if len(input_s) == 0:
                return 'Empty String'
            else:
                return ''.join(input_s)

s = input().strip()
result = super_reduced_string(s)
print(result)
