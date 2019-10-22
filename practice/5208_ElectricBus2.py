# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2


import sys
sys.stdin = open('input/5208.txt')


def backtrack(curr, Sum):
    global arr, Min

    if Sum > Min:
        return

    if arr[curr] >= (arr[0] - curr):
        if Sum < Min:
            Min = Sum
        return
    else:
        for i in range(1, arr[curr]+1):
            backtrack(curr+i, Sum+1)


for T in range(int(input())):
    arr = list(map(int, input().split()))

    Min = arr[0]-1
    backtrack(1, 0)

    print(f"#{T+1} {Min}")