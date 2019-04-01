# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

import sys
sys.stdin = open('../Input/5251.txt', 'r')

"""
# source, destination, length

# start: node 0
# goal: node N
"""

def min_not_vis(vis, dis):
    min_idx = -1
    min_dis = 11111
    for i in range(N+1):
        if vis[i]:
            continue
        else:
            if dis[i] < min_dis:
                min_dis = dis[i]
                min_idx = i
    return min_idx


TC = int(input())
for T in range(1, TC+1):
    N, E = map(int, input().split())  # N+1 nodes including 0, E edges

    edges = [[] for _ in range(N+1)]
    for _ in range(E):  # E edges
        tmp = list(map(int, input().split()))
        edges[tmp[0]] += [(tmp[1], tmp[2])]

    dis = [0] + [11111 for _ in range(N)]  # start at 0; max given weight is 10
    vis = [0]*(N+1)

    while 0 in vis:  # c: current node; run while() until all nodes are marked visited
        c = min_not_vis(vis, dis)
        vis[c] = 1
        for x in edges[c]:
            if dis[c] + x[1] < dis[x[0]]:
                dis[x[0]] = dis[c] + x[1]

    print(f"#{T} {dis[-1]}")






