import sys
sys.stdin = open('Input/input1220.txt', 'r')

"""
5. Stack 2

1220. [S/W 문제해결 기본] 5일차 - Magnetic


"""

for T in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    cnt = 0

    for c in range(N): # search each column
        tmp = 0
        for r in range(N):
            if arr[r][c] == "1":
                tmp = 1
            elif arr[r][c] == "2" and tmp:
                cnt += 1
                tmp = 0

    print(f"#{T} {cnt}")