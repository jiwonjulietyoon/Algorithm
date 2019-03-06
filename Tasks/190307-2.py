# 2001. 파리 퇴치

import sys
sys.stdin = open('../Input/input2001.txt', 'r')

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            Sum = 0
            for k in range(M):
                Sum += sum(arr[i+k][j:j+M])
            if Sum > Max:
                Max = Sum

    print("#{} {}".format(T+1, Max))