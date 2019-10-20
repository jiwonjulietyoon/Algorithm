

import sys
sys.stdin = open('../Input/2573.txt', 'r')

"""
Every year:
1. each iceberg square melts (depending on surrounding env.)
2. count number of icebergs (BFS) => the moment a second iceberg is found, quit program and print answer
    - if there are no more iceberg pieces left, print 0

"""
# direction: 0up 1right 2down 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def melt():
    global arr, R, C
    new = [[0]*C for _ in range(R)]
    for i in range(1, R-1):
        for j in range(1, C-1):
            if arr[i][j]:
                cnt = 0
                for d in range(4):
                    if not arr[i+dr[d]][j+dc[d]]:
                        cnt += 1
                if arr[i][j] > cnt:
                    new[i][j] = arr[i][j] - cnt
    for r in range(1, R-1):
        arr[r][1:C-1] = new[r][1:C-1]


def count():
    global arr, R, C
    vis = [[0]*C for _ in range(R)]
    q = []
    tmp = 0
    for i in range(1, R-1):
        for j in range(1, C-1):
            if not vis[i][j]:
                vis[i][j] = 1
                if arr[i][j]:
                    if tmp:
                        return "break"
                    tmp = 1
                    q.append((i, j))
                    while q:
                        r, c = q.pop()
                        for d in range(4):
                            y, x = r+dr[d], c+dc[d]
                            if not vis[y][x] and arr[y][x]:
                                vis[y][x] = 1
                                q.append((y, x))
    if tmp == 1:
        return "one"
    elif tmp == 0:
        return "zero"

def solve():
    yr = 0
    while 1:
        yr += 1
        melt()
        res = count()
        if res == "break":
            return yr
        elif res == "zero":
            return 0


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

print(solve())






