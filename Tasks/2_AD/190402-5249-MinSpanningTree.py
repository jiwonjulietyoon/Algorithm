# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리


import sys
sys.stdin = open('../Input/5249.txt', 'r')


"""
MST - Prim
since 1 <= V <= 1000 and 1 <= E <= 1,000,000
(Kruksal might not be fast enough with too many edges)

Vertice: 0 ~ V  ( V+1 vertices )

"""


TC = int(input())
for T in range(1, TC+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        tmp = list(map(int, input().split()))
        edges[tmp[0]] += [(tmp[1], tmp[2])]
        edges[tmp[1]] += [(tmp[0], tmp[2])]

    sel = [0]*(V+1)  # selected vertices
    total = 0  # total weight
    cnt = 0  # number of selected edges
    sel[0] = 1  # start at arbitrary vertex and mark it as selected
    while cnt <= V-1:
        end = -1  # end point of next min-weight edge to select
        Min = 11  # min-weight of next edge to select
        for i in range(V+1):
            if sel[i]:
                for edge in edges[i]:
                    if not sel[edge[0]]:
                        if edge[1] < Min:
                            Min = edge[1]
                            end = edge[0]
        total += Min
        cnt += 1
        sel[end] = 1

    print(f"#{T} {total}")