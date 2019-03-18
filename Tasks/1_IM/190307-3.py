# 1979. 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('../Input/input1979.txt', 'r')

for T in range(int(input())):
    N, K = map(int, input().split())
    arr = [input().split() for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0  # row
        for j in range(N):
            if arr[i][j] == "1":  # white square
                cnt += 1
            else:  # black square
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1
        cnt = 0  # column
        for j in range(N):
            if arr[j][i] == "1":
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1

    print("#{} {}".format(T+1, ans))