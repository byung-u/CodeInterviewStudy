#!/usr/bin/env python3
import sys
from collections import deque


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        side = deque()
        n = int(input())
        side.extend(list(map(int, input().split())))
        # print(T, n, side)
        cur_pop = 0
        while len(side) > 1:
            if side[0] > side[-1]:
                if side[0] > cur_pop and cur_pop != 0:
                    # print('[1]No', side[0], cur_pop)
                    print('No')
                    break
                cur_pop = side.popleft()
            elif side[0] < side[-1]:
                if side[-1] > cur_pop and cur_pop != 0:
                    # print('[2]No', side[-1], cur_pop)
                    print('No')
                    break
                cur_pop = side.pop()
            elif side[0] == side[-1]:
                if side[-1] > cur_pop and cur_pop != 0:
                    # print('[3]No', side[-1], cur_pop)
                    print('No')
                    break
                side.popleft()
                cur_pop = side.pop()
        else:
            print('Yes')
