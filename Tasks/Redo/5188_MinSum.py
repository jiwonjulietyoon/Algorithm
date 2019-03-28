
import sys
sys.stdin = open('../Input/5188.txt', 'r')

# direction: 0right 1down
dr = [0, 1]
dc = [1, 0]


def backtrack(i, j, Sum):
    global arr, N, Min
    if Sum > Min:
        return
    if i == N-1 and j == N-1:  # goal
        Sum += arr[i][j]
        if Sum < Min:
            Min = Sum
    elif i == N-1:
        backtrack(i, j+1, Sum+arr[i][j])
    elif j == N-1:
        backtrack(i+1, j, Sum+arr[i][j])
    else:
        for d in range(2):
            backtrack(i+dr[d], j+dc[d], Sum+arr[i][j])


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min = sum(arr[0]) + sum(arr[i][N-1] for i in range(1, N))
    backtrack(0, 0, 0)

    print(f"#{T+1} {Min}")
