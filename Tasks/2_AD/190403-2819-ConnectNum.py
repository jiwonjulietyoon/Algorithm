# 2819. 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open('../Input/2819.txt', 'r')

# direction: 0up, 1right, 2down, 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def DFS(i, j, s):
    global seq, arr
    if len(s) == 7:
        seq.add(s)
    else:
        for d in range(4):
            r, c = i+dr[d], j+dc[d]
            if 0 <= r < 4 and 0 <= c < 4:
                DFS(r, c, s+arr[r][c])

for T in range(1, int(input())+1):
    arr = [0]*4
    for i in range(4):
        arr[i] = input().split()

    seq = set()

    for i in range(4):
        for j in range(4):
            DFS(i, j, arr[i][j])

    print(f"#{T} {len(seq)}")
