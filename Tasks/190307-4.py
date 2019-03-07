# 1211. [S/W 문제해결 기본] 2일차 - Ladder2

import sys
sys.stdin = open('../Input/input1211.txt', 'r')


for _ in range(10):
    T = input()
    arr = [input().split() for _ in range(100)]

    # 0down, 1right, 2left
    dc = [0, 1, -1]
    dr = [1, 0, 0]
    d = 0  # initial direction: down

    Min = 10000  # shortest route
    ans = -1  # starting idx of shortest route

    for i in range(100):
        if arr[0][i] == "1":
            r, c = 1, i
            cnt = 1
            while 1:
                if d == 0:  # going down
                    if c < 99 and arr[r][c+1] == "1":
                        d = 1
                    elif c > 0 and arr[r][c-1] == "1":
                        d = 2
                else:
                    if arr[r+1][c] == "1":
                        d = 0
                r, c = r + dr[d], c + dc[d]
                cnt += 1
                if cnt == Min:
                    break
                if r == 98:
                    Min, ans = cnt, i
                    break

    print("#{} {}".format(T, ans))





