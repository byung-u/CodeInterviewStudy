#!/usr/bin/env python3
import sys
from functools import reduce
from collections import OrderedDict

if __name__ == '__main__':
    
    N = int(input())
    item_and_price = OrderedDict()
    for _ in range(N):
        temp = input().split()
        item_name = reduce(lambda x, y: str(x) + ' ' + str(y), temp)
        item_and_price[item_name] = item_and_price.get(item_name, 0) + 1

    for key, val in item_and_price.items():
        keys = key.split()
        item_name = reduce(lambda x, y: str(x) + ' ' + str(y), keys[0:-1])
        price = int(keys[-1]) * val
        print(item_name, price)
