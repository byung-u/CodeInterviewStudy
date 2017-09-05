#!/usr/bin/env python3


import sys

def timeConversion(s):
    if (s[-2:] == 'AM'):
        temp = int(s[0:2])
        if temp < 10:
            res = '0' + str(temp)
        else:
            res = str(temp)
        if res == '12':
            res = '00'
        return res + s[2:8]
    else:
        temp = s[0:2]
        res = str(int(temp) + 12)
        if res == '24':
            res = '12'
        return res + s[2:8]
    # Complete this function

s = input().strip()
result = timeConversion(s)
print(result)

