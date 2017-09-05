#!/usr/bin/env python3

def  findNumber(arr, k):
    for i in range(0, k):
        if arr[i] > arr[i + 1]:
            return 'NO'
    return 'YES'

_arr_cnt = 0
_arr_cnt = int(input())
_arr_i=0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(input());
    _arr.append(_arr_item)
    _arr_i+=1



_k = int(input());

res = findNumber(_arr, _k)
print(res)
