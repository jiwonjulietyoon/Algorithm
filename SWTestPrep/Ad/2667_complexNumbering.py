# 단지 번호 붙이기

import sys
sys.stdin = open('../Input/2667.txt', 'r')

"""
queue and bfs
"""

def find(i, j, N):
    global vis, arr
    bldg = 1
    q_r = [i]
    q_c = [j]

    while q_r and q_c:
        r = q_r.pop(0)
        c = q_c.pop(0)
        if (r > 0 and arr[r - 1][c]) and not vis[r - 1][c]:
            vis[r-1][c] = 1
            bldg += 1
            q_r.append(r-1)
            q_c.append(c)
        if (c < N-1 and arr[r][c+1]) and not vis[r][c+1]:
            vis[r][c+1] = 1
            bldg += 1
            q_r.append(r)
            q_c.append(c+1)
        if (r < N-1 and arr[r+1][c]) and not vis[r+1][c]:
            vis[r+1][c] = 1
            bldg += 1
            q_r.append(r+1)
            q_c.append(c)
        if (c > 0 and arr[r][c-1]) and not vis[r][c-1]:
            vis[r][c-1] = 1
            bldg += 1
            q_r.append(r)
            q_c.append(c-1)

    return bldg


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

vis = [[0]*N for _ in range(N)]
cnt = []

for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            vis[i][j] = 1
            if arr[i][j]:
                cnt.append(find(i, j, N))

cnt.sort()
print(len(cnt))
print(*cnt, sep="\n")




###################################################
# incorrect

# def find(i, j, N):
#     global vis, arr
#     bldg = 1
#     r, c = i, j
#     print(r, c)
#     s_r = [r]
#     s_c = [c]
#
#     while s_r and s_c:
#         if (r > 0 and arr[r-1][c]) and not vis[r-1][c]:
#             r -= 1
#             print("up", r, c)
#             vis[r][c] = 1
#             bldg += 1
#             s_r.append(r)
#             s_c.append(c)
#         elif (c < N-1 and arr[r][c+1]) and not vis[r][c+1]:
#             c += 1
#             print("right", r, c)
#             vis[r][c] = 1
#             bldg += 1
#             s_r.append(r)
#             s_c.append(c)
#         elif (r < N-1 and arr[r+1][c]) and not vis[r+1][c]:
#             r += 1
#             print("down", r, c)
#             vis[r][c] = 1
#             bldg += 1
#             s_r.append(r)
#             s_c.append(c)
#         elif (c > 0 and arr[r][c-1]) and not vis[r][c-1]:
#             c -= 1
#             print("left", r, c)
#             vis[r][c] = 1
#             bldg += 1
#             s_r.append(r)
#             s_c.append(c)
#         else:
#             r = s_r.pop()
#             c = s_c.pop()
#     return bldg
#
#
# N = int(input())
# arr = [list(map(int, list(input()))) for _ in range(N)]
#
# vis = [[0]*N for _ in range(N)]
#
# cnt = []
#
# for i in range(N):
#     for j in range(N):
#         if not vis[i][j]:
#             vis[i][j] = 1
#             if arr[i][j]:
#                 cnt.append(find(i, j, N))
#
# cnt.sort()
# print(len(cnt))
# print(*cnt, sep="\n")




