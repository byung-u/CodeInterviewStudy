#!/usr/bin/env python3

import sys

def split_and_join(line):
    # write your code here
    line_list = line.split()
    return '-'.join(line_list)

if __name__ == '__main__':
    print(split_and_join('this is a string'))
