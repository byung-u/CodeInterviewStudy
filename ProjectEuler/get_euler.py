#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bs4 import BeautifulSoup
from requests import get, codes


def match_soup_class(target, mode='class'):
    def do_match(tag):
        classes = tag.get(mode, [])
        return all(c in classes for c in target)
    return do_match


def main():
    if len(sys.argv) == 1:
        print('need problem number')
        sys.exit(1)
    else:
        p = int(sys.argv[1])
    file_name = 'euler_%d.py' % p
    with open(file_name, 'w') as f:

        url = 'https://projecteuler.net/problem=%d' % p
        r = get(url)
        if r.status_code != codes.ok:
            print('[url request failed] ', url)
            return
        soup = BeautifulSoup(r.text, 'html.parser')
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write("\n'''")
        problem = '\nProblem %d' % p
        f.write(problem)
        for content in soup.find_all(match_soup_class(['problem_content'])):
            f.write(content.text)
        f.write("'''\n\n")
        msg = 'def p%d():\n' % p
        f.write(msg)
        f.write('    return\n\n\n')
        msg = 'p%d()\n' % p
        f.write(msg)
    f.closed


if __name__ == '__main__':
    main()
