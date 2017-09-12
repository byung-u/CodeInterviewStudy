#!/usr/bin/env python2

if __name__ == '__main__':
    for i in range(1,int(input())):
        print(((10 ** i - 1) / 9) * i)
        # print(int(''.join([str(i) for j in range(1 , i + 1)])))
