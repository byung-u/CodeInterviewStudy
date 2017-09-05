#!/usr/bin/env python3


def solve(grades):
    result = []
    for g in grades:
        c = g % 10 - 5
        if g < 38:
            result.append(g)
        elif c == -2 or c == 3:
            result.append(g + 2)
        elif c == -1 or c == 4:
            result.append(g + 1)
        else:
            result.append(g)
    return result


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
