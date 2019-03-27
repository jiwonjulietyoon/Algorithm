"""
5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
"""

import sys
sys.stdin = open('../Input/5203.txt', 'r')

"""
RUN: 3+ consecutive numbers
TRIPLET: 3+ identical numbers

each player needs to have at least 3 cards before attempting to determine the winner

"""

def check_run(p):   # return boolean
    p = list(set(p))
    if len(p) < 3:
        return 0
    p.sort()
    for i in range(len(p)-2):
        if p[i] + 1 == p[i+1] and p[i+1] + 1 == p[i+2]:
            return 1
    return 0

def check_triplet(p):
    for x in set(p):
        if p.count(x) == 3:
            return 1
    return 0

def play(num, p1, p2):
    for i in range(8):
        if not i%2: # even (incl. 0) => player 1
            p1.append(num[i])
            if check_run(p1):
                return "1"
            if check_triplet(p1):
                return "1"
        else: # odd => player 2
            p2.append(num[i])
            if check_run(p2):
                return "2"
            if check_triplet(p2):
                return "2"
    return "0"

for T in range(int(input())):
    num = list(map(int, input().split()))
    p1 = [num[0], num[2]]
    p2 = [num[1], num[3]]
    num = num[4:]

    print(f"#{T+1} {play(num, p1, p2)}")


