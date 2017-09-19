#!/usr/bin/env python3

def capitalize(string):
    s = string.split(' ')
    for i in range(0, len(s)):
        if len(s[i]) == 0:
            continue
        if len(s[i][0]) != 0 and s[i][0].isalpha():
            s[i] = s[i].title()
    return ' '.join(s)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
