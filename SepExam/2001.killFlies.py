# 2001. 파리 퇴치 D2

import sys
sys.stdin = open('input/2001.txt')


for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    Max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            res = 0
            for k in range(M):
                res += sum(arr[i+k][j:j+M])
            if res > Max:
                Max = res
    print("#{} {}".format(T, Max))