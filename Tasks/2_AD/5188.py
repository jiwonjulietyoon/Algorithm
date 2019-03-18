# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

"""
# start: arr[0][0]
# end : arr[N-1][N-1]

Recursive + backtracking + pruning

"""

import sys
sys.stdin = open('../Input/5188.txt', 'r')


# right, down
dr = [0, 1]
dc = [1, 0]

def backtrack(r, c, Sum):   # r, c: current row and column
    global arr, N, Min
    if r == N-1 and c == N-1:
        if Sum < Min:
            Min = Sum
    if Sum > Min:
        return
    if r == N-1 and c < N-1:  # right
        backtrack(r, c+1, Sum+arr[r][c+1])
    elif r < N-1 and c == N-1:  # down
        backtrack(r+1, c, Sum+arr[r+1][c])
    elif r < N-1 and c < N-1:  # right or down
        for d in range(2):
            r, c = r+dr[d], c+dc[d]
            Sum += arr[r][c]
            backtrack(r, c, Sum)
            Sum -= arr[r][c]
            r, c = r-dr[d], c-dc[d]


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 130
    backtrack(0, 0, arr[0][0])
    print(f"#{T+1} {Min}")



