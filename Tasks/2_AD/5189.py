# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

"""
1번: 사무실

- start off with 1(사무실) marked as visited
- after all spots are visited, finish off by visiting 1 again

- keep track of current spot and previous spot


"""

import sys
sys.stdin = open('../Input/5189.txt', 'r')

def backtrack(p, c, Sum):  # current, previous
    global arr, N, Min, vis
    if 0 not in vis:
        Sum += arr[c-1][0]
        if Sum < Min:
            Min = Sum
    if Sum > Min:
        return
    for i in range(2, N+1):
        if not vis[i]:
            c = i
            vis[c] = 1
            Sum += arr[p-1][c-1]
            p = c
            pp = p
            backtrack(p, c, Sum)
            p = pp
            c = p
            Sum -= arr[p - 1][c - 1]
            vis[i] = 0





for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min = 10000
    vis = [1] + [0]*N
    vis[1] = 1

    backtrack(1, 1, 0)

    print(f"#{T+1} {Min}")

