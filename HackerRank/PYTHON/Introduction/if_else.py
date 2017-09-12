#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    if n & 1:   # odd
        print('Weird')
    else:
        if 6 < n <= 20:
            print('Weird')
        else:
            print('Not Weird')
