
# 블록맞추기

import sys
sys.stdin = open('../Input/2652.txt', 'r')

"""
- read through arr and find all blocks (use visited arr)
- save the top-left corner cell info of each block in separate arr (to print answer)

- for each block cells, find four corner cells (min r min c / max r min c ... )
- from these four corners, find rectangular dimension
- from each corner, (start from top left corner) count how many '1's in each side


Find out if the 'ㅗ' block fits anywhere:
- u == either width or height of the block




"""

#################################################################

""" Receive Inputs  """

N = int(input())   # arr size
u, v, w, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


################################################################

"""  Find all blocks in arr and each of their dimensions  """

vis = [[0]*N for _ in range(N)]
blocks = []  # all cells of each block
dim = []  # dimension of each block  : (y1, y2, x1, x2, width, height)

# direction: 0up 1right 2down 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            vis[i][j] = 1
            if arr[i][j]:
                blocks.append([(i, j)])  # add new list
                y1 = y2 = i  # min, Max
                x1 = x2 = j  # min, Max
                q = [(i, j)]
                while q:
                    r, c = q.pop()
                    for d in range(4):
                        y, x = r+dr[d], c+dc[d]
                        if 0 <= y < N and 0 <= x < N:
                            if arr[y][x] and not vis[y][x]:
                                blocks[-1].append((y, x))
                                vis[y][x] = 1
                                q.append((y, x))
                                if y < y1:
                                    y1 = y
                                if y > y2:
                                    y2 = y
                                if x < x1:
                                    x1 = x
                                if x > x2:
                                    x2 = x
                dim.append((y1, y2, x1, x2, x2-x1+1, y2-y1+1))

print(*blocks, sep="\n")
print()
print(*dim, sep="\n")

################################################################

"""  Check each block to see if it fits  """

n = len(dim)  # total number of blocks found
cnt = 0  # number of blocks that fit
ans = []  # top left cell of blocks that fit

for i in range(n):  # go through each block
    y1, y2, x1, x2, w, h = dim[i]
    if u not in [w, h]:  # ㅗblock won't fit
        continue
    # blocks[i], dim[i]
    # top, bot => width  //  left, right => height
    top = arr[y1][x1:x2+1]
    bot = arr[y2][x1:x2+1]
    right = [arr[q][x2] for q in range(y1, y2+1)]
    left = [arr[q][x1] for q in range(y1, y2+1)]
    print(top, right, bot, left)

    s = 0
    for side in [top, right, bot, left]:
        if 0 in side:   # s = 0top, 1right, 2bot, 3left
            L = w if s in [0, 2] else h
            o1 = z = 0
            for i in range(L):
                if side[i] == 1:
                    o1 += 1
                else:
                    break
            for j in range(i, L):
                if side[j] == 0:
                    z += 1
                else:
                    break
        s += 1
    print(o1, z)
    if w != o1 or y != z:
        continue

    depth = 0  # depth of hollowed part
    if s == 0:









# edges = [[] for _ in range(n)]

# for i in range(n):
#     edges[i] += sum(arr[dim[i][0]][dim[i][2]:dim[i][3]+1]) # top side
#     edges[i] += sum(arr[mi][mj:Mj+1])
#     edges[i] += sum(arr[mi][mj:Mj+1])




##############################################################

"""  Print answer  """

# print(cnt)
# for a in ans:
#     print(*a)
