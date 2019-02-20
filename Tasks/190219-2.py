# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로


def maze(arr, N, r, c):
    if arr[r][c] == "3":    # goal
        return 1
    elif arr[r][c] == "1":   # wall
        return 0
    elif arr[r][c] == "-1":  # visited
        return 0

    arr[r][c] = "-1"        # visited

    if ((c < N - 1 and maze(arr, N, r, c+1))      # right
        or (r > 0 and maze(arr, N, r-1, c))   # up
        or (c > 0 and maze(arr, N, r, c-1))   # left
        or (r < N - 1 and maze(arr, N, r+1, c))):  # down
        return 1

    return 0


for T in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    tmp = False
    for R in range(N):
        for C in range(N):
            if arr[R][C] == "2":
                r, c = R, C
                tmp = True
                break
        if tmp:
            break

    print(f"#{T + 1} {maze(arr, N, r, c)}")

























#########################################################

