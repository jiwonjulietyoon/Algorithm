# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

import sys
sys.stdin = open('../Input/5201.txt', 'r')


"""
eliminate any w greater than max(t)


"""


for T in range(int(input())):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))   # weights of N containers
    trucks = list(map(int, input().split()))   # capacity of M trucks
    weights.sort(reverse=True)
    trucks.sort(reverse=True)

    total = 0

    for w in weights:
        for t in trucks:
            if w <= t:
                trucks.remove(t)
                total += w
                break

    print(f"#{T+1} {total}")





