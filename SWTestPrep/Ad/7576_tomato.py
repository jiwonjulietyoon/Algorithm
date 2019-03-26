

import sys
# sys.stdin = open('../Input/7576_1.txt', 'r')
sys.stdin = open('../Input/7576_2.txt', 'r')

"""

 1 : ripe tomato
 0 : unripe tomato
-1 : no tomato

"""
# direction: 0up, 1right, 2down, 3left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isUnripe(arr, R, C):  # return Boolean
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '0':  # when any unripe tomato is found
                return 1
    return 0

def findRipe(arr, R, C):  # find currently ripe tomatoes
    res = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "1":
                res.append((i, j))
    return res

def ripe(q):
    global arr, R, C
    new = set()
    for t in q:
        for d in range(4):
            r, c = t[0]+dr[d], t[1]+dc[d]
            if 0 <= r < R and 0 <= c < C:
                if arr[r][c] == '0':
                    new.add((r, c))
    new = list(new)
    for x in new:
        arr[x[0]][x[1]] = '1'  # mark 'ripe'
    return new

def solve(q):
    global arr, R, C
    if not isUnripe(arr, R, C):  # all tomatoes are ripe
        return 0
    days = 0
    while q:
        days += 1
        q = ripe(q)
    if not isUnripe(arr, R, C):
        return days-1
    else:
        return -1

C, R = map(int, input().split())
arr = [input().split() for _ in range(R)]
print(solve(findRipe(arr, R, C)))  # findRipe: ripe tomatoes at the start






####################################################################
# Time over

# # direction: 0up, 1right, 2down, 3left
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# def ripe():    # keep track of any changes?
#     global arr, R, C
#     new = [[] for _ in range(R)]
#     for i in range(R):
#         new[i] = arr[i][:]
#     cnt = 0  # number of unripe tomatoes after one more cycle
#     change = 0  # whether or not there have been any changes
#     for i in range(R):
#         for j in range(C):
#             if arr[i][j] == '0':   # only look at unripened tomatoes
#                 tmp = 1  # unripe tomato found
#                 for d in range(4):  # for all possible directions
#                     r, c = i+dr[d], j+dc[d]
#                     if 0 <= r < R and 0 <= c < C:  # only when within range
#                         if arr[r][c] == '1':
#                             new[i][j] = '1'
#                             tmp = 0  # tomato is now ripe
#                             change = 1
#                             break
#                 if tmp:
#                     cnt += 1
#     # after traversing through all cells:
#     for i in range(R):
#         arr[i] = new[i][:]   # copy row by row
#     return cnt, change
#
#
# def unripe(arr, R, C):   # Are there any unripe tomatoes?
#     for i in range(R):
#         for j in range(C):
#             if arr[i][j] == '0':  # the moment an unripe tomato is encountered
#                 return 1
#     return 0
#
#
# def solve():
#     global arr, R, C
#     if not unripe(arr, R, C):
#         return 0
#     days = 0
#     while 1:
#         days += 1
#         cnt, change = ripe()
#         if cnt == 0:
#             return days
#         if change == 0:
#             return -1
#
#
# C, R = map(int, input().split())
# arr = [input().split() for _ in range(R)]
#
# print(solve())

