# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

import sys
sys.stdin = open('../Input/5185.txt', 'r')

for T in range(int(input())):
    _, num = input().split()
    res = ''
    for x in range(len(num)):
        res += bin(int(num[x], 16))[2:].zfill(4)
    print("#{} {}".format(T+1, res))


#####################################################

