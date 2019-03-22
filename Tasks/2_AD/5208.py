# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

import sys
sys.stdin = open('../Input/5208.txt', 'r')

"""
<Variables>
c : current position
p : power left

"""

def backtrack(c, Sum):
    global Min, M, N
    if Sum > Min:
        return
    if M[c] >= N-c:  # goal reached
        if Sum < Min:
            Min = Sum  # replace record minimum
    else:  # need to charge



for T in range(int(input())):
    tmp = list(map(int, input().split()))
    N = tmp[0] - 1
    M = tmp[1:]

    Min = N   # record minimum charges

    backtrack(0, 0)


    print(f"#{T+1} {Min}")


