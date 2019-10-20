""" 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

"""


import sys
sys.stdin = open('input/5188.txt')

def backtrack(r, c, Sum):  # r, c : current position coordinates
    global arr, Min, N

    # pruning
    if Sum > Min:
        return

    if r == N-1 and c == N-1:  # goal reached
        if Sum < Min:  # minimum record broken
            Min = Sum
        return
    else:
        if r == N-1:  # can only move right
            backtrack(r, c+1, Sum+arr[r][c+1])
        elif c == N-1:  # can only move down
            backtrack(r+1, c, Sum+arr[r+1][c])
        else:  # can move either right or down
            backtrack(r+1, c, Sum+arr[r+1][c])
            backtrack(r, c+1, Sum+arr[r][c+1])


for T in range(int(input())):
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # Calculate possible min value
    Min = sum(arr[0])
    for i in range(1, N):
        Min += arr[N-1][i]

    # Start off with arr[0][0]
    backtrack(0, 0, arr[0][0])

    print(f"#{T+1} {Min}")

