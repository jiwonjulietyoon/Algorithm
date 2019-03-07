import sys
sys.stdin = open('Input/input1210.txt', 'r')

"""
4. Stack 1

1210. [S/W 문제해결 기본] 2일차 - Ladder1

start at "2"

only move up, right, or left

"""



for T in range(10):
    _ = input()
    arr = [ input().split() for _ in range(100) ]

    r, c = 99, arr[99].index("2") # start

    # 0up, 1right, 2left
    dx = [0, 1, -1]
    dy = [-1, 0, 0]
    d = 0 # initial direction: up

    while 1:
        r, c = r + dy[d], c + dx[d]
        if r == 0:
            break
        if d == 0: # while moving up
            if (c < 99) and arr[r][c+1] == "1":
                d = 1 # change direction to right
            elif (c > 0) and arr[r][c-1] == "1":
                d = 2 # change direction to left
        else: # while moving left or right
            if arr[r-1][c] == "1":
                d = 0 # change direction to up

    print(f"#{T+1} {c}")