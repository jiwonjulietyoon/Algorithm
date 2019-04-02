# 5521. 상원이의 생일파티

import sys
sys.stdin = open('../Input/5521.txt', 'r')


TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a] += [b]
        edges[b] += [a]

    sel = [0] + [0]*N
    q = [1]
    sel[1] = 1

    for _ in range(2):
        tmp, q = q[:], []
        for x in tmp:
            for num in edges[x]:
                if not sel[num]:
                    sel[num] = 1
                    q.append(num)

    print(f"#{T} {sum(sel)-1}")