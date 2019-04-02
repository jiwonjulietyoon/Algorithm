# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

import sys
sys.stdin = open('../Input/5247.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')

""" +1, -1, *2, -10
N => M
"""


TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split())

    cnt = 0
    vis = [0]*1000001

    q = [N]
    while 1:
        cnt += 1
        tmp, q = q, []
        for num in tmp:
            new = [num-1, num+1, num*2, num-10]
            for x in new:
                if 1 <= x <= 1000000 and not vis[x]:
                    q.append(x)
                    vis[x] = 1
        print(q)
        if M in q:
            break

    print(f"#{T} {cnt}")



#########################################
# Time Out

# TC = int(input())
# for T in range(1, TC+1):
#     N, M = map(int, input().split())
#
#     cnt = 0
#
#     q = [N]
#     while 1:
#         cnt += 1
#         tmp, q = q[:], []
#         for num in tmp:
#             if 1 <= num-1 <= 1000000:
#                 q.append(num-1)
#             if 1 <= num+1 <= 1000000:
#                 q.append(num+1)
#             if 1 <= num*2 <= 1000000:
#                 q.append(num*2)
#             if 1 <= num-10 <= 1000000:
#                 q.append(num-10)
#         q = list(set(q))
#         if M in q:
#             break
#
#     print(f"#{T} {cnt}")

















# less = [-10, -1]

# def solve(res, cnt):
#     global N, M, Min
#     if (cnt > Min) or (res < 0) or (res > 1000000):
#         return
#     if (abs(M-res) == 1) or (res*2 == M) or (res-10 == M):
#         cnt += 1
#         if cnt < Min:
#             Min = cnt
#     elif M > res:   # try +1 or *2
#         for i in range(2):
#             solve(res+1, cnt+1)
#             solve(res*2, cnt+1)
#     elif res > M:  # try -1 or -10
#         for i in range(2):
#             solve(res+less[i], cnt+1)
#     else:  # when res == M?
#         return
#
#
#
# for T in range(int(input())):
#     N, M = map(int, input().split())
#
#     d = N - M
#     # when N > M : need to decrease
#     if 0 < d < 10:  # cnt == d  (using only -1)
#         print(f"#{T+1} {d}")
#     elif d >= 10:
#         print(f"#{T+1} {sum(divmod(d, 10))}")  # incorrect for certain cases
#     else:  # need to increase
#
#
#     print(f"#{T+1} {solve(N, M)}")



