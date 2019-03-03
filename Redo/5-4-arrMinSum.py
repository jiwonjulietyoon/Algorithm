import sys
sys.stdin = open('Input/input4881.txt', 'r')

"""
5. Stack 2

4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합


"""

def minSum(r, Sum): # r: current row
    global arr, N, sel, Min

    if r == N:
        if Sum < Min:
            Min = Sum
        return

    if Sum > Min:
        return

    for c in range(N):
        if not sel[c]:
            Sum += arr[r][c]
            sel[c] = 1
            minSum(r+1, Sum)
            Sum -= arr[r][c]
            sel[c] = 0

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sel = [0] * N
    Min = 90
    minSum(0, 0)

    print(f"#{T+1} {Min}")