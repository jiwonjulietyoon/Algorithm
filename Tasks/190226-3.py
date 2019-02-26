# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

import sys
sys.stdin = open('input5099.txt', 'r')

def enQueue(item):
    global cQ, rear
    rear = (rear+1) % len(cQ)
    cQ[rear] = item

def deQueue():
    global cQ, front
    front = (front+1) % len(cQ)
    return cQ[front]

for T in range(int(input())):
    N, M = map(int, input().split())
    C = list(enumerate(map(int, input().split()), start=1))

    cQ = [0] * (N+1)
    front = rear = 0

    for i in range(N):
        enQueue([C[i][0], C[i][1]])
    C[:N] = []

    while rear != front:
        pizza = deQueue()
        pizza[1] //= 2
        if pizza[1]:
            enQueue(pizza)
        else:
            if C:
                enQueue([C[0][0], C[0][1]])
                C.pop(0)

    print(f"#{T + 1} {cQ[front][0]}")