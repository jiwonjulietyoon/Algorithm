# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로

import sys
sys.stdin = open('../Input/1247.txt', 'r')

"""
출발: 회사

경로: N명의 고객들

도착: 집

"""


def backtrack(k, p, Sum):
    global cust, coord, vis, Min, N
    if Sum > Min:
        return
    if k == N:
        Sum += abs(cust[p][0]-coord[2]) + abs(cust[p][1]-coord[3])
        if Sum < Min:
            Min = Sum
    else:
        for i in range(1, N+1):
            if not vis[i]:
                vis[i] = 1
                backtrack(k+1, i, Sum + abs(cust[p][0]-cust[i][0]) + abs(cust[p][1]-cust[i][1]))
                vis[i] = 0


for T in range(int(input())):
    N = int(input())
    coord = list(map(int, input().split()))

    cust = [[coord[0], coord[1]]] + [[] for _ in range(N)]
    for i in range(N):
        cust[i+1] = [coord[i*2+4], coord[i*2+5]]

    vis = [1] + [0]*N
    Min = 3000
    backtrack(0, 0, 0)

    print(f"#{T+1} {Min}")



