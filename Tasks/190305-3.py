# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

import sys
sys.stdin = open('../Input/input5177.txt', 'r')


def insertHeap(idx, val):
    global heap, value
    value[idx] = val
    if idx == 1:
        pass
    else:
        if idx % 2: # odd
            heap[idx//2][1] = idx
        else: # even
            heap[idx//2][0] = idx

def checkHeap(idx): # compare: value[idx] (child) and value[idx//2] (parent)
    global heap, value
    while 1:
        if idx == 1:
            break
        if value[idx] < value[idx//2]: # => need to swap parent and child
            value[idx], value[idx//2] = value[idx//2], value[idx]
        idx //= 2

for T in range(int(input())):
    N = int(input())
    num = [None] + list(map(int, input().split()))
    heap = [[0, 0] for _ in range(N+1)]
    value = [None] + [0] * N

    for i in range(1, N+1):
        insertHeap(i, num[i])
        checkHeap(i)

    Sum = 0
    while N > 1:
        N //= 2
        Sum += value[N]
    print("#{} {}".format(T+1, Sum))


