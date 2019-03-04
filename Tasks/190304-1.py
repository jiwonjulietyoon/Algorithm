# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

import sys
sys.stdin = open('../Input/input5174.txt', 'r')


def preorder(T):
    global tree, cnt
    if T:
        cnt += 1
        preorder(tree[T][0])
        preorder(tree[T][1])


for T in range(int(input())):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))

    tree = [ [0, 0] for _ in range(E+2)]

    for i in range(0, len(tmp), 2):
        a, b = tmp[i:i+2]
        if tree[a][0]:
            tree[a][1] = b
        else:
            tree[a][0] = b

    cnt = 0
    preorder(N)

    print("#{} {}".format(T+1, cnt))
