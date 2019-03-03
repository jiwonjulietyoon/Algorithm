import sys
sys.stdin = open('Input/input4875.txt', 'r')

"""
5. Stack 2

4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로


"""

def maze(r, c):
    global arr, N
    if arr[r][c] == "3": # goal
        return 1
    if arr[r][c] == "1": # wall or visited
        return 0

    arr[r][c] = "1" # mark as visited

    # up, right, down, left
    if (r > 0 and maze(r-1, c)) \
        or (c < N-1 and maze(r, c+1)) \
        or (r < N-1 and maze(r+1, c)) \
        or (c > 0 and maze(r, c-1)):
        return 1

    return 0


for T in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    tmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "2":
                tmp = 1
                break
        if tmp:
            break

    print(f"#{T+1} {maze(i, j)}")

