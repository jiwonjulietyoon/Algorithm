# 1238. [S/W 문제해결 기본] 10일차 - Contact

import sys
sys.stdin = open('input1238.txt', 'r')

for T in range(10):
    N, S = map(int, input().split())
    tmp = list(map(int, input().split()))
    nodes = [[] for _ in range(101)]
    for i in range(N//2):
        a, b = tmp[2*i:2*i+2]
        nodes[a] += [b]
    Q = [S]
    vis = [1] + [0] * 100

    while Q:
        tmp = Q[:]
        for nd in tmp:
            vis[nd] = 1
        for nd in tmp:
            for x in nodes[nd]:
                if not vis[x]:
                    Q.append(x)
            Q.remove(nd)

    print(f"#{T+1} {max(tmp)}")