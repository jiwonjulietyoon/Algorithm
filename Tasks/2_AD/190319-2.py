# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

import sys
sys.stdin = open('../Input/5186.txt', 'r')

def binary(N):
    ans = [0] * 12
    for i in range(12):
        tmp = 2**(-1 * (i+1))
        if N >= tmp:
            ans[i] = 1
            N -= tmp
        if N == 0:
            return ans[:i+1]
    return 'overflow'


for T in range(int(input())):
    N = float(input())

    print(f"#{T+1}", end=" ")
    print(*binary(N), sep="")





