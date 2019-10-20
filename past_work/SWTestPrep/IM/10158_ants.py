w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# direction: 0top right, 1top left, 2bottom right, 3bottom left
dp = [1, -1, 1, -1] # x, left right horizontal
dq = [1, 1, -1, -1] # y, up down vertical
d = 0

init = w-p
if init == h-q:
    lap = min(w, h) * 2
    if t <= init:
        p, q = p+t, q+t
    else:
        t = (t-init) % lap
        if t <= lap//2:
            p, q = w - t, h - t
        else:
            plus = t - (lap//2)
            p, q = w - min(w, h) + plus, h - min(w, h) + plus
else:
    ini = min(w - p, h - q)
    if t <= ini:
        p, q = p + t, q + t
    else:
        p, q = p + ini, q + ini
        t -= ini
        while t > 0:
            if (d == 0 and p == w) or (d == 3 and q == 0): # right = curr position
                d = 1 # next direction
                move = min(p, h-q) # spaces to move next
            elif (d == 0 and q == h) or (d == 3 and p == 0): # top
                d = 2
                move = min(w-p, q)
            elif (d == 1 and p == 0) or (d == 2 and q == 0): # left
                d = 0
                move = min(w - p, h - q)
            elif (d == 1 and q == h) or (d == 2 and p == w): # top
                d = 3
                move = min(p, q)
            p, q = p+(dp[d]*move), q+(dq[d]*move)
            t -= move
        if t < 0:
            p, q = p + (dp[d] * t), q + (dq[d] * t)

print(p, q)









#############################################################


# # direction: 0top right, 1top left, 2bottom right, 3bottom left
# dp = [1, -1, 1, -1] # x, left right horizontal
# dq = [1, 1, -1, -1] # y, up down vertical
# d = 0
#
# for _ in range(t):
#     if 0 < p < w:
#         if q == h:
#             d = 2 if d == 0 else 3
#         elif q == 0:
#             d = 0 if d == 2 else 1
#     elif 0 < q < h:
#         if p == w:
#             d = 1 if d == 0 else 3
#         elif p == 0:
#             d = 2 if d == 3 else 0
#     elif p == w:
#         d = 3 if q == h else 1
#     elif p == 0:
#         d = 2 if q == h else 0
#     p, q = p + dp[d], q + dq[d]
#
#
# print(p, q)











####################################################
#시간 초과


# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
#
# # direction: 0top right, 1top left, 2bottom right, 3bottom left
# dp = [1, -1, 1, -1] # x, left right horizontal
# dq = [1, 1, -1, -1] # y, up down vertical
# d = 0
#
# for _ in range(t):
#     if 0 < p < w:
#         if q == h:
#             d = 2 if d == 0 else 3
#         elif q == 0:
#             d = 0 if d == 2 else 1
#     elif 0 < q < h:
#         if p == w:
#             d = 1 if d == 0 else 3
#         elif p == 0:
#             d = 2 if d == 3 else 0
#     elif p == w:
#         d = 3 if q == h else 1
#     elif p == 0:
#         d = 2 if q == h else 0
#     p, q = p + dp[d], q + dq[d]
#
# print(p, q)




####################################################
#시간 초과

# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
#
# # direction: 0top right, 1top left, 2bottom right, 3bottom left
# dp = [1, -1, 1, -1] # x, left right horizontal
# dq = [1, 1, -1, -1] # y, up down vertical
# d = 0
#
# for _ in range(t):
#     if (0 < p < w) and (0 < q < h): # inside
#         pass
#     elif p == w and (0 < q < h): # right side
#         if d == 0:
#             d = 1
#         elif d == 2:
#             d = 3
#     elif p == w and q == h: # top right corner
#         d = 3
#     elif p == w and q == 0: # bottom right corner
#         d = 1
#     elif p == 0 and q == h: # top left corner
#         d = 2
#     elif p == 0 and q == 0: # bottom left corner
#         d = 0
#     elif (0 < p < w) and q == h: # top side
#         if d == 0:
#             d = 2
#         elif d == 1:
#             d = 3
#     elif p == 0 and (0 < q < h): # left side
#         if d == 3:
#             d = 2
#         elif d == 1:
#             d = 0
#     elif (0 < p < w) and q == 0: # bottom side
#         if d == 2:
#             d = 0
#         elif d == 3:
#             d = 1
#     p, q = p + dp[d], q + dq[d]
#
# print(p, q)





