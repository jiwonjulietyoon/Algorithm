# 5650. [모의 SW 역량테스트] 핀볼 게임

import sys
sys.stdin = open('Input/5650.txt', 'r')
# sys.stdin = open('Input/tmp.txt', 'r')

"""
- Use Backtracking (DFS + Pruning)
- Track current row, col, direction

0: pass
-1: black hole
1-5: block (square or triangular)
6-10: wormhole

wall: switch to opposite direction
game ends when ball returns to starting point or meets black hole

"""

# direction: 0up, 1right, 2down, 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def opp_dir(d):  # returns opposite direction
    return (d + 2) % 4

def game(i, j, d, cnt):
    global Max
    while 1:
        if i < 0 or i >= N or j < 0 or j >= N:  # wall
            d = opp_dir(d)
            cnt += 1
        elif arr[i][j] == -1 or (i == si and j == sj):  # game over
            if cnt > Max:
                Max = cnt
            return
        elif not arr[i][j]:  # pass
            pass
        elif 1 <= arr[i][j] <= 5:  # block
            if arr[i][j] == 5:
                d = opp_dir(d)
            elif arr[i][j] == 1:
                if d == 1 or d == 0:
                    d = opp_dir(d)
                elif d == 2:
                    d = 1
                else:
                    d = 0
            elif arr[i][j] == 2:
                if d == 2 or d == 1:
                    d = opp_dir(d)
                elif d == 0:
                    d = 1
                else:
                    d = 2
            elif arr[i][j] == 3:
                if d == 2 or d == 3:
                    d = opp_dir(d)
                elif d == 1:
                    d = 2
                else:
                    d = 3
            else:  # block 4
                if d == 0 or d == 3:
                    d = opp_dir(d)
                elif d == 2:
                    d = 3
                else:
                    d = 0
            cnt += 1
        elif 6 <= arr[i][j] <= 10:  # wormhole
            for k in range(2):
                if [i, j] == worm[arr[i][j]-6][k]:
                    i, j = worm[arr[i][j]-6][1-k]
                    break
        i += dr[d]
        j += dc[d]


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [0] * N
    worm = [[] for _ in range(5)]  # wormhole coordinates: 0-6, 1-7, 2-8, 3-9, 4-10
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                worm[arr[i][j]-6] += [[i, j]]

    Max = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                continue
            for d in range(4):
                si, sj = i, j  # starting point
                game(i+dr[d], j+dc[d], d, 0)

    print(f"#{T} {Max}")






###########################################################################
# incorrect: Recursion => Maximum recursion limit

# # direction: 0up, 1right, 2down, 3left
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# def opp_dir(d):  # returns opposite direction
#     return (d+2) % 4
#
# def game(i, j, d, cnt):
#     global Max
#     # print(i, j, d, cnt)
#     if i < 0 or i >= N or j < 0 or j >= N:  # wall
#         d = opp_dir(d)
#         game(i+dr[d], j+dc[d], d, cnt+1)
#     elif arr[i][j] == -1 or (i == si and j == sj):  # game over
#         # print(si, sj, "end")
#         if cnt > Max:
#             Max = cnt
#             # print(Max)
#         return
#     elif not arr[i][j]:  # pass
#         game(i+dr[d], j+dc[d], d, cnt)
#     elif 1 <= arr[i][j] <= 5: # block
#         if arr[i][j] == 5:
#             d = opp_dir(d)
#         elif arr[i][j] == 1:
#             if d == 1 or d == 0:
#                 d = opp_dir(d)
#             elif d == 2:
#                 d = 1
#             else:
#                 d = 0
#         elif arr[i][j] == 2:
#             if d == 2 or d == 1:
#                 d = opp_dir(d)
#             elif d == 0:
#                 d = 1
#             else:
#                 d = 2
#         elif arr[i][j] == 3:
#             if d == 2 or d == 3:
#                 d = opp_dir(d)
#             elif d == 1:
#                 d = 2
#             else:
#                 d = 3
#         else:  # block 4
#             if d == 0 or d == 3:
#                 d = opp_dir(d)
#             elif d == 2:
#                 d = 3
#             else:
#                 d = 0
#         game(i+dr[d], j+dc[d], d, cnt+1)
#     elif 6 <= arr[i][j] <= 10:  # wormhole
#         for w in worm[arr[i][j]-6]:
#             if i != w[0] and j != w[1]:
#                 break
#
#         game(w[0]+dr[d], w[1]+dc[d], d, cnt)
#
#
# for T in range(1, int(input())+1):
#     N = int(input())
#     arr = [0]*N
#     worm = [[] for _ in range(5)]  # wormhole coordinates: 0-6, 1-7, 2-8, 3-9, 4-10
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#         for j in range(N):
#             if 6 <= arr[i][j] <= 10:
#                 worm[arr[i][j]-6] += [[i, j]]
#
#     Max = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 continue
#             for d in range(4):
#                 si, sj = i, j  # starting point
#                 game(i+dr[d], j+dc[d], d, 0)
#
#     print(f"#{T} {Max}")