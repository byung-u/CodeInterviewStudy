#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import count, combinations
from math import factorial

from util import (is_palindromic, prime_sieve, is_prime, is_triangle,
                  is_square, is_pentagonal, is_hexagonal, is_heptagonal,
                  is_octagonal)


'''
Problem 51
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''
def check_rp(num_str, input_num):
    if num_str.count('0') >= 2:
        num_str_len = len(num_str)
        p_found = [j for j in range(num_str_len) if num_str[j] == '0']
        comb = combinations(p_found, 2)
        for c in comb:
            diff = 10 ** (num_str_len -1 - c[0])
            diff += 10 ** (num_str_len -1 - c[1])
            rp = [(input_num + k * diff) for k in range(0, 10) if is_prime(input_num + (k * diff))]
            if len(rp) > 6:
                print(len(rp), rp)
            if len(rp) > 7:
                print(len(rp), rp, i)
                return


def p51():
    # for i in count(140100641, 2):
    for i in count(285304301, 10):
        check_rp(str(i), i)
        check_rp(str(i+2), i + 2)  # 3
        check_rp(str(i+6), i + 6)  # 7
        check_rp(str(i+8), i + 8)  # 9

'''
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''


def p52():
    i = 125875
    while(1):
        str_i = str(i)
        if len(str_i) != len(set(str_i)):
            i += 1
            continue
        comp_num = sorted(str_i)
        for j in range(2, 7):
            if comp_num != sorted(str(i * j)):
                break
            else:
                if j == 6:
                    print('[52]: ', i)
                    return
        if(str_i[0] != '1'):  # MUST number start 1
            i *= 5  # 2000 * 5 = 10000
        else:
            i += 1


'''
Problem 53
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,

nCr = n!r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''


def p53():
    ret = []
    for r in range(1, 101):
        for n in range(r, 101):
            c = (factorial(n) / (factorial(r) * factorial(n - r)))
            if c > 1000000:
                ret.append(str(n) + str(r))
    print('[53]: ', len(ret))


'''
Problem 54
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins;
    for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie,
    for example, both players have a pair of queens,
    then highest cards in each hand are compared (see example 4 below);
    if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand Player 1 Player 2 Winner
1 5H 5C 6S 7S KDPair of Fives 2C 3S 8S 8D TDPair of Eights Player 2
2 5D 8C 9S JS ACHighest card Ace 2C 5C 7D 8S QHHighest card Queen Player 1
3 2D 9C AS AH ACThree Aces 3D 6D 7D TD QDFlush  with Diamonds Player 2
4 4D 6S 9H QH QCPair of QueensHighest card Nine 3D 6D 7H QD QSPair of QueensHighest card Seven Player 1
5 2H 2D 4C 4D 4SFull HouseWith Three Fours 3C 3D 3S 9S 9DFull Housewith Three Threes Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
'''


ROYAL_FLUSH = 110
STRAIGHT_FLUSH = 109
FOUR_OF_KIND = 108
FULL_HOUSE = 107
FLUSH = 106
STRAIGHT = 105
THREE_OF_KIND = 104
TWO_PAIR = 103
ONE_PAIR = 102


def pocker_point(card):
    # 스-다-하-클
    nums = []
    suit = []
    for c in card:  # pocker.txt does not have 10
        if c[0] == 'T':
            nums.append(10)
        elif c[0] == 'J':
            nums.append(11)
        elif c[0] == 'Q':
            nums.append(12)
        elif c[0] == 'K':
            nums.append(13)
        elif c[0] == 'A':
            nums.append(14)
        else:
            nums.append(int(c[0]))
        suit.append(c[1])
    nums = sorted(nums)
    suit = sorted(suit)
    # print(nums, suit)
    if nums == ['10', '11', '12', '13', '14'] and len(set(suit)) == 1:
        return ROYAL_FLUSH, 14, 0  # Royal Flush
    elif len(set(suit)) == 1:
        if ( int(nums[0]) + 1 == int(nums[1]) and
             int(nums[1]) + 1 == int(nums[2]) and
             int(nums[2]) + 1 == int(nums[3]) and
             int(nums[3]) + 1 == int(nums[4])):
            return STRAIGHT_FLUSH, nums[4], nums[3]
        else:
            return FLUSH, max(nums), 0
    elif ( nums[0] == nums[3] or
           nums[1] == nums[4]):
        return FOUR_OF_KIND, nums[2], 0
    elif len(set(nums)) == 2:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        return FULL_HOUSE, d[max(d, key=d.get)], d[min(d, key=d.get)]
    elif ( int(nums[0]) + 1 == int(nums[1]) and
           int(nums[1]) + 1 == int(nums[2]) and
           int(nums[2]) + 1 == int(nums[3]) and
           int(nums[3]) + 1 == int(nums[4])):
        return STRAIGHT, nums[4], 0
    elif ( nums[0] == nums[2] or
           nums[1] == nums[3] or
           nums[2] == nums[4]):
        return THREE_OF_KIND, nums[2], 0
    elif len(set(nums)) == 3:
        return TWO_PAIR, nums[3], 0
    elif len(set(nums)) == 4:
        max_num = 0
        if nums[0] == nums[1]:
            max_num = nums[1]
        elif nums[1] == nums[2]:
            max_num = nums[2]
        elif nums[2] == nums[3]:
            max_num = nums[3]
        elif nums[3] == nums[4]:
            max_num = nums[4]
        return ONE_PAIR, max_num, 0
    else:
        return nums[4], nums[4], 0


def p54():
    p1_win = 0
    with open('pocker.txt') as f:
        for line in f:
            p = line.strip('\n').split(' ')
            p1, max_p1, pp1 = pocker_point(p[:5])
            p2, max_p2, pp2 = pocker_point(p[5:])
            print(p1, p2, p[:5], p[5:])
            if p1 > p2:
                p1_win += 1
            elif p1 == p2:
                if max_p1 > max_p2:
                    p1_win += 1
                elif max_p1 == max_p2:
                    if pp1 > pp2:
                        p1_win += 1
                    else:
                        print(line)  # need compare h/d/c/s
    print('[54]: ', p1_win)


'''
Problem 55
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.

Due to the theoretical nature of these numbers, and for the purpose of this problem,
we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand,
it will either
    (i) become a palindrome in less than fifty iterations, or,
    (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
    4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
'''


def p55():
    ret = []
    for i in range(1, 10000):
        num = i
        for j in range(1, 50):
            num = num + int(str(num)[::-1])
            if is_palindromic(str(num)):
                ret.append(i)
                break
    print('[55]: ', 10000 - (len(ret) + 1))


'''
Problem 56
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''


def p56():
    ret = []
    for a in range(80, 100):
        if a % 10 == 0:
            continue
        for b in range(80, 100):
            c = a ** b
            ret.append(sum(list(map(int, str(c)))))

    print('[56]: ', max(ret))


'''
Problem 57
It is possible to show that the square root of two can be expressed
as an infinite continued fraction.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''


def p57():
    cnt = 0
    n = 1  # numerator
    d = 2  # denominator
    for i in range(2, 1001):
        temp_n = n
        n = d
        d = (2 * d) + temp_n
        res_n = n + d
        if len(str(res_n)) != len(str(d)):
            cnt += 1
            print(res_n, d)
    print('[57]: ', cnt)


'''
Problem 58
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49



37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued,
what is the side length of the square spiral for which the ratio of primes along both diagonals
first falls below 10%?
'''


def p58():
    lying = 1 + 4
    p1, p2, p3, p4 = 1, 1, 1, 1
    prime_cnt = 0

    for i, spiral in enumerate(count(3, 2)):

        p1 = p1 + (8 * i) + 2  # left up
        p2 = p2 + (8 * i) + 8  # right up
        p3 = p3 + (8 * i) + 4  # left down
        p4 = p4 + (8 * i) + 6  # right down
        if is_prime(p1):
            prime_cnt += 1
        if is_prime(p2):
            prime_cnt += 1
        if is_prime(p3):
            prime_cnt += 1
        if is_prime(p4):
            prime_cnt += 1

        ratio = prime_cnt * 100 / lying
        # print([spiral], p1, p2, p3, p4, '\t', prime_cnt, lying, ratio)
        if ratio < 10:
            print('[58]: ', spiral)
            return
        lying += 4


'''
Problem 59
Each character on a computer is assigned a unique code and the preferred standard is
ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text;
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users,
so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely,
the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge
that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
'''


def p59():
    cipher = [int(x) for x in open('cipher.txt').read().strip('\n').split(',')]
    passwd = []
    # A: 65, Z: 90, a: 97, z: 122
    english = list(range(65, 91)) + list(range(97, 123))
    for i in range(3):  # key = three lower case
        enc = [c for idx, c in enumerate(cipher) if idx % 3 == i]
        temp_pw = []
        max_dec = 0
        for j in range(97, 122 + 1):
            temp_dec = [e for e in enc if e ^ j in english]
            if max_dec < len(temp_dec):
                max_dec = len(temp_dec)
                temp_pw = j
        passwd.append(temp_pw)
    dec = [c ^ passwd[i % 3] for i, c in enumerate(cipher)]
    print('[59]: ', sum(dec))


'''
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
# (13, 5197, 5701, 6733, 8389)


def p60():  # pretty bad  ㅜ.ㅜ
    # ret = []
    for i in range(3, 1000, 2):
        if i == 5:
            continue
        if is_prime(i) is False:
            continue

        for j in range(7, 10000, 2):
            if is_prime(j) is False:
                continue
            chk = '%d%d' % (i, j)
            if is_prime(int(chk)) is False:
                continue
            chk = '%d%d' % (j, i)
            if is_prime(int(chk)) is False:
                continue

            for k in range(109, 10000, 2):
                if is_prime(k) is False:
                    continue
                chk = '%d%d' % (k, i)
                if is_prime(int(chk)) is False:
                    continue
                chk = '%d%d' % (i, k)
                if is_prime(int(chk)) is False:
                    continue
                chk = '%d%d' % (j, k)
                if is_prime(int(chk)) is False:
                    continue
                chk = '%d%d' % (k, j)
                if is_prime(int(chk)) is False:
                    continue

                for l in range(673, 10000, 2):
                    if is_prime(l) is False:
                        continue
                    chk = '%d%d' % (l, i)
                    if is_prime(int(chk)) is False:
                        continue
                    chk = '%d%d' % (i, l)
                    if is_prime(int(chk)) is False:
                        continue
                    chk = '%d%d' % (j, l)
                    if is_prime(int(chk)) is False:
                        continue
                    chk = '%d%d' % (l, j)
                    if is_prime(int(chk)) is False:
                        continue
                    chk = '%d%d' % (k, l)
                    if is_prime(int(chk)) is False:
                        continue
                    chk = '%d%d' % (l, k)
                    if is_prime(int(chk)) is False:
                        continue

                    for m in range(677, 10000, 2):
                        if is_prime(m) is False:
                            continue
                        chk = '%d%d' % (m, i)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (i, m)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (j, m)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (m, j)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (k, m)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (m, k)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (l, m)
                        if is_prime(int(chk)) is False:
                            continue
                        chk = '%d%d' % (m, l)
                        if is_prime(int(chk)) is False:
                            continue
                        print ('[60]: ', (i + j + k + l+ m))
                        return
                        # found = (i, j, k, l, m)
                        # ret.append(found)
    return


'''
Problem 61
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle
 
P3,n=n(n+1)/2
 
1, 3, 6, 10, 15, ...
Square
 
P4,n=n2
 
1, 4, 9, 16, 25, ...
Pentagonal
 
P5,n=n(3n−1)/2
 
1, 5, 12, 22, 35, ...
Hexagonal
 
P6,n=n(2n−1)
 
1, 6, 15, 28, 45, ...
Heptagonal
 
P7,n=n(5n−3)/2
 
1, 7, 18, 34, 55, ...
Octagonal
 
P8,n=n(3n−2)
 
1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281,
has three interesting properties.
The set is cyclic, in that the last two digits of each number
is the first two digits of the next number
(including the last number with the first).
Each polygonal type:
    triangle   (P3,127=8128),
    square     (P4, 91=8281),
    pentagonal (P5 ,44=2882),
is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
    triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
    is represented by a different number in the set.
'''


def p61():
    triangle = []
    square = []
    pentagonal = []
    hexagonal = []
    heptagonal = []
    octagonal = []
    for i in range(1000, 10000):
        if is_triangle(i):
            triangle.append(i)
        if is_square(i):
            square.append(i)
        if is_pentagonal(i):
            pentagonal.append(i)
        if is_hexagonal(i):
            hexagonal.append(i)
        if is_heptagonal(i):
            heptagonal.append(i)
        if is_octagonal(i):
            octagonal.append(i)

    polygonals = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    for i, polygonal in enumerate(polygonals):
        for num in polygonal:
            tail_num1 = num % 100  # 8231 -> 31
            head_num1 = num // 100  # 8231 -> 82

            for j, polygonal in enumerate(polygonals):
                if i == j:
                    continue
                for num2 in polygonal:
                    head_num2 = num2 // 100  # 8231 -> 82
                    if tail_num1 != head_num2:
                        continue
                    tail_num2 = num2 % 100  # 8231 -> 31

                    for k, polygonal in enumerate(polygonals):
                        if i == k or j == k:
                            continue
                        for num3 in polygonal:
                            head_num3 = num3 // 100  # 8231 -> 82
                            if tail_num2 != head_num3:
                                continue
                            tail_num3 = num3 % 100  # 8231 -> 31

                            for l, polygonal in enumerate(polygonals):
                                if i == l or j == l or k == l:
                                    continue
                                for num4 in polygonal:
                                    head_num4 = num4 // 100  # 8231 -> 82
                                    if tail_num3 != head_num4:
                                        continue
                                    tail_num4 = num4 % 100  # 8231 -> 31

                                    for m, polygonal in enumerate(polygonals):
                                        if i == m or j == m or k == m or l == m:
                                            continue
                                        for num5 in polygonal:
                                            head_num5 = num5 // 100  # 8231 -> 82
                                            if tail_num4 != head_num5:
                                                continue
                                            tail_num5 = num5 % 100  # 8231 -> 31

                                            for n, polygonal in enumerate(polygonals):
                                                if i == n or j == n or k == n or l == n or m == n:
                                                    continue
                                                for num6 in polygonal:
                                                    head_num6 = num6 // 100  # 8231 -> 82
                                                    if tail_num5 != head_num6:
                                                        continue
                                                    tail_num6 = num6 % 100  # 8231 -> 31
                                                    if tail_num6 == head_num1:
                                                        print(num, num2, num3, num4, num5, num6)
                                                        print('[61]: ', num + num2 + num3 + num4 + num5 + num6)
                                                        return


'''
Problem 62
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
'''


def p62():
    cubes = [i ** 3 for i in range(1, 10001)]
    find_key = 0
    d = {}
    for c in cubes:
        check_num = ''.join(sorted(list(str(c))))
        d[check_num] = d.get(check_num, 0) + 1

    for key, val in d.items():
        if val == 5:
            find_key = key
            break

    find_cube = [c for c in cubes if ''.join(sorted(list(str(c)))) == find_key]
    print('[62]: ', min(find_cube))


'''
Problem 63
The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
'''


def p63():
    total = 0
    for i in range(1, 10):
        for j in count(1):
            k = i ** j
            if len(str(k)) == j:
                total += 1
            elif len(str(k)) < j:
                break
    print('[63]: ', total)
    return


'''
Problem 64
All square roots are periodic when written as continued fractions
and can be written in the form:

It can be seen that the sequence is repeating.
For conciseness, we use the notation √23 = [4;(1,3,1,8)],
to indicate that the block (1,3,1,8) repeats indefinitely.
The first ten continued fraction representations of (irrational) square roots are:

    √2=[1;(2)], period=1
    √3=[1;(1,2)], period=2
    √5=[2;(4)], period=1
    √6=[2;(2,4)], period=2
    √7=[2;(1,1,1,4)], period=4
    √8=[2;(1,4)], period=2
    √10=[3;(6)], period=1
    √11=[3;(3,6)], period=2
    √12= [3;(2,6)], period=2
    √13=[3;(1,1,1,1,6)], period=5 <-- odd period

Exactly four continued fractions, for N ≤ 13, have an odd period.
How many continued fractions for N ≤ 10000 have an odd period?
'''


'''
Problem 65
The square root of 2 can be written as an infinite continued fraction.
2 + ...

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].
It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.


Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

'''
Problem 66
Consider quadratic Diophantine equations of the form:
x2 – Dy2 = 1
For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''



'''
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

def p67():
    tri = []
    with open('triangle.txt') as f:
        for line in f:
            p = line.split()
            tri.append(list(map(int, p)))
    rtri = [tri[i] for i in reversed(range(0, len(tri)))]
    len_tri = len(rtri) - 1
    for i in range(0, len_tri):
        for j in range(0, len_tri - i):
            rtri[i+1][j] = max(rtri[i][j] + rtri[i+1][j] , rtri[i][j+1] + rtri[i+1][j])
    print('[67]: ', rtri[99][0])
    return


'''
Problem 68
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

TotalSolution Set
94,2,3; 5,3,1; 6,1,2
94,3,2; 6,2,1; 5,1,3
102,3,5; 4,5,1; 6,1,3
102,5,3; 6,3,1; 4,1,5
111,4,6; 3,6,2; 5,2,4
111,6,4; 5,4,2; 3,2,6
121,5,6; 2,6,4; 3,4,5
121,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''



'''
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n Relatively Prime φ(n) n/φ(n)
2 1             1 2
3 1,2           2 1.5
4 1,3           2 2
5 1,2,3,4       4 1.25
6 1,5           2 3
7 1,2,3,4,5,6   6 1.1666...
8 1,3,5,7       4 2
9 1,2,4,5,7,8   6 1.5
10 1,3,7,9      4 2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''


def p69():
    # number has most primes devidor is the answer
     # 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510
     # 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 = 9699690
    print('[69]: ', 2 * 3 * 5 * 7 * 11 * 13 * 17)


'''
Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1. 
Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 10^7,
for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''


'''
Problem 71
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''
'''
Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''
'''
Problem 73
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

'''
Problem 74
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''


def check_74_factorial(factorials, i, str_i):
    check = []
    check.append(i)
    cnt = 0
    while (1):
        cnt += 1
        if cnt > 60:
            return 0
        sums = [factorials[int(str_i[j])] for j in range(0, len(str_i))]
        res = sum(sums)
        if res not in check:
            check.append(res)
        else:
            return cnt
        str_i = str(res)


def p74():
    factorials = [factorial(i) for i in range(0, 10)]
    ret = [i for i in range(1000000, 1, -1) if check_74_factorial(factorials, i, str(i)) == 60]
    print('[74]: ', len(ret))


'''
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
12 cm: (3,4,5)24 cm: (6,8,10)30 cm: (5,12,13)36 cm: (9,12,15)40 cm: (8,15,17)48 cm: (12,16,20)
In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
120 cm: (30,40,50), (20,48,52), (24,45,51)
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
'''
Problem 76
It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?
'''


'''
Problem 77
It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

'''
Problem 78
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(6)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
'''