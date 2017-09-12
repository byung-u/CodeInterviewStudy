#!/usr/bin/env python2

if __name__ == '__main__':
    for i in range(1,int(input())+1):
        print((10 ** i - 1) ** 2 // 81)

    # Weired.. This one is alse one line
    for i in range(1,int(input())+1):
        print(int(''.join([str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)])))

    '''
    for i in range(1,int(input())+1):
        for j in range(1, i * 2):
            if j > i:
                k -= 1
                print(k , end='')
            elif j == i:
                k = j
                print(j , end='')
            else:
                print(j , end='')
        print()
    '''
