"""
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

"""


import sys
sys.stdin = open('input/5189.txt')


def backtrack(curr, Sum, k):
    global arr, N, vis, Min

    # pruning
    if Sum > Min:
        return

    if k == N:  # goal
        Sum += arr[curr][0]
        if Sum < Min:
            Min = Sum
        return
    else:
        for i in range(1, N):
            if not vis[i]:
                vis[i] = 1
                backtrack(i, Sum+arr[curr][i], k+1)
                vis[i] = 0


for T in range(int(input())):
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    Min = 1000  # 100 * 10
    vis = [1] + [0] * (N-1)  # Mark 사무실 as visited

    backtrack(0, 0, 1)

    print(f"#{T+1} {Min}")