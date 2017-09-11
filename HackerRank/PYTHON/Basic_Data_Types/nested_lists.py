#!/usr/bin/env python3

import sys
import operator

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        temp = []
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        students.append(temp)

    min_val = min(students, key=operator.itemgetter(1))
    filtered_students = []
    for s in students:
        if min_val[1] == s[1]:
            continue
        filtered_students.append(s)

    min_val = min(filtered_students, key=operator.itemgetter(1))
    result = []
    for s in filtered_students:
        if s[1] == min_val[1]:
            result.append(s[0])
    result = sorted(result)
    for r in result:
        print(r)
