# 4615. 재미있는 오셀로 게임

import sys
sys.stdin = open('../Input/input4615.txt', 'r')



def othello(color, opp, r, c): # color: disk color / opp: other color
    global arr, N
    arr[r][c] = color
    # N
    if r >= 2 and arr[r-1][c] == opp:
        for i in range(r-2, -1, -1):
            if arr[i][c] == 0:
                break
            if arr[i][c] == color:
                for k in range(i+1, r):
                    arr[k][c] = color
                break
    # NE
    if (r >= 2 and c <= N-3) and arr[r-1][c+1] == opp:
        m = min(r-1, N-c-2)
        for i in range(2, m+2):
            if arr[r-i][c+i] == 0:
                break
            if arr[r-i][c+i] == color:
                for k in range(i):
                    arr[r-k][c+k] = color
                break
    # NW
    if (r >= 2 and c >= 2) and arr[r-1][c-1] == opp:
        m = min(r-1, c-1)
        for i in range(2, m+2):
            if arr[r-i][c-i] == 0:
                break
            if arr[r-i][c-i] == color:
                for k in range(i):
                    arr[r-k][c-k] = color
                break
    # W
    if c >= 2 and arr[r][c-1] == opp:
        for j in range(c-2, -1, -1):
            if arr[r][j] == 0:
                break
            if arr[r][j] == color:
                for k in range(j+1, c):
                    arr[r][k] = color
                break
    # E
    if c <= N-3 and arr[r][c+1] == opp:
        for j in range(c+2, N):
            if arr[r][j] == 0:
                break
            if arr[r][j] == color:
                for k in range(c+1, j):
                    arr[r][k] = color
                break
    # S
    if r <= N-3 and arr[r+1][c] == opp:
        for i in range(r+2, N):
            if arr[i][c] == 0:
                break
            if arr[i][c] == color:
                for k in range(r+1, i):
                    arr[k][c] = color
                break
    # SW
    if (r <= N-3 and c >= 2) and arr[r+1][c-1] == opp:
        m = min(N-r-2, c-1)
        for i in range(2, m+2):
            if arr[r+i][c-i] == 0:
                break
            if arr[r+i][c-i] == color:
                for k in range(i):
                    arr[r+k][c-k] = color
                break
    # SE
    if (r <= N-3 and c <= N-3) and arr[r+1][c+1] == opp:
        m = min(N-r-2, N-c-2)
        for i in range(2, m+2):
            if arr[r+i][c+i] == 0:
                break
            if arr[r+i][c+i] == color:
                for k in range(i):
                    arr[r+k][c+k] = color
                break

for T in range(int(input())):
    N, M = map(int, input().split()) # N: arr size, M: number of rounds
    disks = [list(map(int, input().split())) for _ in range(M)] # 1: bl / 2: wh

    arr = [[0]*N for _ in range(N)]
    mid = N // 2 - 1
    arr[mid][mid], arr[mid + 1][mid + 1] = 2, 2  # white
    arr[mid + 1][mid], arr[mid][mid + 1] = 1, 1  # black

    for disk in disks:
        if disk[2] == 1:  # black
            othello(1, 2, disk[1]-1, disk[0]-1)
        else:  # white
            othello(2, 1, disk[1]-1, disk[0]-1)

    bl = wh = 0  # counts
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                bl += 1
            elif arr[i][j] == 2:
                wh += 1

    print("#{} {} {}".format(T+1, bl, wh))

