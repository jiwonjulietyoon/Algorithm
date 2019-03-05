# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합


import sys
sys.stdin = open('../Input/input5178.txt', 'r')


for T in range(int(input())):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]

    val = [None] + [0]*N
    for x in leaf:
        val[x[0]] = x[1]

    for i in range(N, 0, -1):
        if not val[i]:
            if i*2+1 <= N:
                val[i] = val[i*2] + val[i*2+1]
            else:
                val[i] = val[i * 2]

    print("#{} {}".format(T+1, val[L]))

