#!/usr/bin/env python3

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        ret = []
        for s in string[i:i + k]:
            if s in ret:
                continue
            ret.append(s)
        print(''.join(ret))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
