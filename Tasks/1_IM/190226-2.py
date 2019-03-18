# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

import sys
sys.stdin = open('input5105.txt', 'r')

def maze(r, c):
    global arr, N, cnt

    if arr[r][c] == '3': # goal
        return 1
    elif arr[r][c] == '1': # wall
        return 0
    elif arr[r][c] == '-1': # visited
        return 0

    arr[r][c] = '-1'   # mark current spot as visited

    # up, right, down, left
    if ((r > 0) and (maze(r-1, c))) \
            or ((c < N-1) and (maze(r, c+1))) \
            or ((r < N-1) and (maze(r+1, c))) \
            or ((c > 0) and (maze(r, c-1))):
        cnt += 1
        return 1

    return 0

for T in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    tmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                tmp = 1
                break
        if tmp:
            break

    cnt = 0
    maze(i, j)
    cnt -= 1 if cnt > 0 else 0

    print(f"#{T + 1} {cnt}")