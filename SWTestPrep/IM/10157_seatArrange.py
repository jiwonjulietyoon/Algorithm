# 자리 배정

import sys
sys.stdin = open('../Input/10157.txt', 'r')
#
#
# C, R = map(int, input().split())  # C: 가로 -> W, R: 세로 -> H
# K = int(input())
#
# # number of layers
# # m = min(C, R)
# # q, r = divmod(m, 2)
# # layers = q + r
#
# w, h = C-1, R
# layers = [0, (w+h)*2-2]
# w -= 2
# h -= 2
#
# print(layers)
#
# while w > 0 and h > 0:
#     tmp = layers[-1] + (w+h)*2-2
#     if tmp > K:
#         break
#     layers.append(tmp)
#     w -= 2
#     h -= 2
#
# # K is in len(layers)th layer
# w += 2
# h += 2
# sub = [(w+h)*2-2, 2*w+h-1, w+h, w]
# for i in range(4):
#     if K < sub[i]:
#         break
#
#
# print(K-sub[i], i)
#
#
# print(layers)
# print(w, h)
# print(sub)

# print(x, y)












#########################################################
# 시간 초과

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    cnt = 1

    x, y = 1, 1  # starting position // # R = 6, C = 7
    xs, xe = 1, C
    ys, ye = 1, R
    d = 'u'  # u, r, d, l

    while cnt < K:
        if cnt < K:  # up
            cnt += ye - y
            y = ye
            xs += 1
            d = 'u'
        if cnt < K:  # right
            cnt += xe - x
            x = xe
            ye -= 1
            d = 'r'
        if cnt < K:  # down
            cnt += y - ys
            y = ys
            xe -= 1
            d = 'd'
        if cnt < K:  #left
            cnt += x - xs
            x = xs
            ys += 1
            d = 'l'

    more = cnt-K
    if more > 0:
        if d == 'u':
            y -= more
        elif d == 'd':
            y += more
        elif d == 'r':
            x -= more
        elif d == 'l':
            x += more

    print(x, y)

















####################################################################
# 시간 초과


# C, R = map(int, input().split())
# K = int(input())
#
# arr = [[0]*C for _ in range(R)]
#
# # direction: 0up, 1right, 2down, 3left
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# d = 0
#
# cnt = 1
# r, c = R-1, 0  # starting position
# arr[r][c] = 1
#
# while cnt < K:
#     if d == 0:
#         if r > 0 and not arr[r-1][c]:
#             pass
#         else:
#             d = 1
#     elif d == 1:
#         if c < C-1 and not arr[r][c+1]:
#             pass
#         else:
#             d = 2
#     elif d == 2:
#         if r < R-1 and not arr[r+1][c]:
#             pass
#         else:
#             d = 3
#     else:
#         if c > 0 and not arr[r][c-1]:
#             pass
#         else:
#             d = 0
#     r, c = r+dr[d], c+dc[d]
#     cnt += 1
#     arr[r][c] = 1
#
# print(c+1, R-r)

