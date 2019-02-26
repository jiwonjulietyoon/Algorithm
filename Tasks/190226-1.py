# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전


# ############################################
# using queue:

import sys
sys.stdin = open('input5097.txt', 'r')

def enQueue(item):
    global Q, rear
    rear += 1
    Q[rear] = item

def deQueue():
    global Q, front
    front += 1
    return Q[front]

for T in range(int(input())):
    N, M = map(int, input().split())
    num = input().split()

    Q = [0] * (M + N)
    front = rear = -1
    for i in range(N):
        enQueue(num[i])
    for _ in range(M):
        tmp = deQueue()
        enQueue(tmp)

    print(f"#{T+1} {Q[front+1]}")





###########################################
# for T in range(int(input())):
#     N, M = map(int, input().split())
#     num = input().split()
#     M = M % N
#     print(f"#{T+1} {num[M]}")