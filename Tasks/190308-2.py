# 4615. 재미있는 오셀로 게임

import sys
sys.stdin = open('../Input/input4615.txt', 'r')

def othello(color, opp, r, c): # color: disk color / opp: other color
    global arr, N
    # N
    if r > 0 and arr[r-1][c] == opp:
        for i in range(r-2, -1, -1):
            if arr[i][c] == 0:
                break
            if arr[i][c] == color:
                for k in range(r-1, i):
                    arr[k][c] = color
                break
    # NE
    if (r > 0 and c < N-1) and arr[r-1][c+1] == opp:
        for i in range()

    # NW
    if (r > 0 and c > 0) and arr[r-1][c-1] == opp:

    # W
    if c > 0 and arr[r][c-1] == opp:

    # E
    if c < N-1 and arr[r][c+1] == opp:

    # S
    if r < N-1 and arr[r+1][c] == opp:

    # SW
    if (r < N-1 and c > 0) and arr[r+1][c-1] == opp:

    # SE
    if (r < N-1 and c < N-1) and arr[r+1][c+1] == opp:



for T in range(int(input())):
    N, M = map(int, input().split()) # N: arr size, M: number of rounds
    disks = [list(map(int, input().split())) for _ in range(M)]
    # 1: bl / 2: wh

    arr = [[0]*N for _ in range(N)]
    mid = N // 2 - 1
    arr[mid][mid], arr[mid + 1][mid + 1] = 2, 2  # white
    arr[mid + 1][mid], arr[mid][mid + 1] = 1, 1  # black

    for disk in disks:
        if disk[2] == 1:  # black
            othello(1, 2, disk[1]-1, disk[0]-1)
        else:  # white
            othello(2, 1, disk[1]-1, disk[0]-1)



    print(arr)


    # print("#{} {} {}".format(T+1, bl, wh))

