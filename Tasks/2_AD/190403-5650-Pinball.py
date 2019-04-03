# 5650. [모의 SW 역량테스트] 핀볼 게임

import sys
sys.stdin = open('../Input/5650.txt', 'r')

"""
- Use Backtracking (DFS + Pruning)
- Track current row, col, direction

0: pass
-1: black hole
1-5: block (square or triangular)
6-10: wormhole

wall: switch to opposite direction

"""

# direction: 0up, 1right, 2down, 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


for T in range(1, int(input())+1):
    N = int(input())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    print(*arr, sep="\n")

    for i in range(N):
        for j in range(N):
            if arr[i][j]
            for d in range()





    # print(f"#{T} {Max}")