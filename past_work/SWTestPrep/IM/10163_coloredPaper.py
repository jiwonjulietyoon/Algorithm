# 색종이

"""


- last rectangle: entirely visible

"""

import sys
sys.stdin = open('../Input/10163.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

mx, my = paper[0][0], paper[0][1]  # minimum x and y coordinates
for i in range(1, N):
    if paper[i][0] < mx:
        mx = paper[i][0]
    if paper[i][1] < my:
        my = paper[i][1]

arr = [[0]*101 for _ in range(101)]

for p in range(N):
    x, y, w, h = paper[p]
    x -= mx
    y -= my
    for i in range(y, y+h):
        for j in range(x, x+w):
            arr[i][j] = p+1

cnt = [0]*(N+1)

for i in range(101):
    for j in range(101):
        if arr[i][j]:
            cnt[arr[i][j]] += 1

for i in range(1, N+1):
    print(cnt[i])







#################################################################
# 1st try

# N = int(input())
# rec = [list(map(int, input().split())) for _ in range(N)]
#
# area = [0] * N
#
# for r in range(N):
#     x, y, w, h = rec[r]
#     area[r] = w*h
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             for p in range(r-1, -1, -1):
#                 if area[p] == 0:
#                     break
#                 x0, y0, w0, h0 = rec[p]
#                 if (x0 <= i < x0+w0) and (y0 <= j < y0+h0):
#                     area[p] -= 1
#                     break
#
# print(*area, sep="\n")



#####################################################################################



# N = int(input())
# rec = [list(map(int, input().split())) for _ in range(N)]
#
# coor = [[] for _ in range(N)]
# area = [0] * N
#
# for r in range(N):
#     x, y, w, h = rec[r]
#     area[r] = w*h
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             coor[r].append((i, j))
#             for p in range(r):
#                 if area[p] == 0:
#                     continue
#                 x0, y0, w0, h0 = rec[p]
#                 if (x0 <= i <= x0+w0) and (y0 <= j <= y0+h0) and ((i, j) in coor[p]):
#                     coor[p].remove((i, j))
#                     area[p] -= 1
#                     break
#
# print(*area, sep="\n")






########################################################
#시간 초과

# N = int(input())
# rec = [list(map(int, input().split())) for _ in range(N)]
#
# coor = [[] for _ in range(N)]
#
# for r in range(N):
#     x, y, w, h = rec[r]
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             coor[r].append((i, j))
#             for p in range(r):
#                 if (i, j) in coor[p]:
#                     coor[p].remove((i, j))
#
# for area in coor:
#     print(len(area))

