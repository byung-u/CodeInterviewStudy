#!/usr/bin/env python3

import sys


def count_substring(string, sub_string):
    l1 = len(string)
    l2 = len(sub_string)
    return len([i for i in range(0, l1 - l2 + 1) if (string[i:i+l2] == sub_string)])
    

if __name__ == '__main__':
    string = input()
    sub_string = input()
    print(count_substring(string, sub_string))

