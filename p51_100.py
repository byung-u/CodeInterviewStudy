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


def check_prime_cnt(idx, prime_str):
    d = {}
    p_found = []
    for i in range(len(prime_str)):
        if prime_str[i] == str(idx):
            p_found.append(i)
    if p_found[-1] == len(prime_str) - 1:
        return 0

    comb = combinations(p_found, 2)
    for c in comb:
        cnt = 0
        temp = list(map(str, prime_str))
        for i in range(0, 10):
            if i == 0:
                if c[0] == 0:
                    continue
            # if (9 - i) + cnt < 8:
                # break
            temp[c[0]] = str(i)
            temp[c[1]] = str(i)
            if is_prime(int(''.join(temp))):
                cnt += 1
                d[int(''.join(temp))] = cnt
    if len(d) == 0:
        return 0
    if 6 < d[max(d, key=d.get)]:
        print(prime_str, d[max(d, key=d.get)])
    return d[max(d, key=d.get)]


def p51():
    all_primes = prime_sieve(500000000)
    primes = []
    for p in all_primes:
        str_p = str(p)
        if len(str_p) == len(set(str_p)):
            continue
        primes.append(p)
    prime_len = len(primes)
    # for i in range(1683605, prime_len):  # primes[5780] = 56693
    166278239
    for i in range(5581720, prime_len):  # primes[5780] = 56693
        prime_str = str(primes[i])
        prime_cnt = prime_str.count('0')
        if prime_cnt >= 2:
            if check_prime_cnt(0, prime_str) == 8:
                print('[51]: ', primes[i])
                return
        prime_cnt = prime_str.count('1')
        if prime_cnt >= 2:
            if check_prime_cnt(1, prime_str) == 8:
                print('[51]: ', primes[i])
                return
        prime_cnt = prime_str.count('2')
        if prime_cnt >= 2:
            if check_prime_cnt(2, prime_str) == 8:
                print('[51]: ', primes[i])
                return


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


def p60():
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
