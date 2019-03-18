# 1959. 두 개의 숫자열

import sys
sys.stdin = open('../Input/input1959.txt', 'r')

def mul(long, short, L, S):
    global Max
    for i in range(L-S+1):
        Sum = 0
        for j in range(S):
            Sum += long[i+j] * short[j]
        if Sum > Max:
            Max = Sum

for T in range(int(input())):
    N, M = map(int, input().split())  # len(A), len(B), respectively
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Max = 0
    mul(A, B, N, M) if N >= M else mul(B, A, M, N)

    print("#{} {}".format(T+1, Max))
