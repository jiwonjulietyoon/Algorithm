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
    for i in range(2, N+1):
        if not vis[i]:
            vis[i] = 1
            c = i
            Sum += arr[p][c]
            p = c
            backtrack(p, c, Sum)





for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min = 10000
    vis = [1] + [0]*N
    vis[1] = 1

    backtrack(1, 1, 0)

    print(f"#{T+1} {Min}")

