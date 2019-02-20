# 1210. [S/W 문제해결 기본] 2일차 - Ladder1













########## 2nd try

for T in range(10):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, arr[99].index(2)

    dr = [-1, 0, 0]
    dc = [0, 1, -1]
    d = 0

    while(1):
        r, c = r + dr[d], c + dc[d]
        if r == 0:
            break
        if d == 0:
            if c != 0 and c != 99:
                if arr[r][c + 1]:
                    d = 1
                elif arr[r][c - 1]:
                    d = 2
            elif c == 0:
                if arr[r][c + 1]:
                    d = 1
            elif c == 99:
                if arr[r][c - 1]:
                    d = 2
        else:
            if arr[r - 1][c]:
                d = 0
    print(f"#{T + 1} {c}")





######### 1st try

for T in range(10):
    _ = input()  # test case number
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, arr[99].index(2)  # current row and col

    dr = [-1, 0, 0]   # 0up, 1right, 2left
    dc = [0, 1, -1]
    d = 0  # initial direction: up

    while(1):
        r = r + dr[d]
        c = c + dc[d]
        if r == 0:
            break
        if d == 0:
            if c != 0 and c != 99:
                if arr[r][c + 1]:
                    d = 1
                elif arr[r][c - 1]:
                    d = 2
            elif c == 0:
                if arr[r][c + 1]:
                    d = 1
            elif c == 99:
                if arr[r][c - 1]:
                    d = 2
        elif d == 1:
            if arr[r - 1][c]:
                d = 0
        elif d == 2:
            if arr[r - 1][c]:
                d = 0
    print(f"#{T + 1} {c}")