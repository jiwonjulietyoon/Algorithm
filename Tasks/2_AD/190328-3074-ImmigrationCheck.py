# 3074. 입국심사



import sys
import time
sys.stdin = open('../Input/3074.txt', 'r')

st = time.time()


TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split())

    times = [0]*N
    for i in range(N):
        times[i] = int(input())

    # binary search
    r = min(times) * M
    l = min(times)

    while l < r:
        m = (l + r) // 2

        Sum = 0
        for i in range(N):
            Sum += m//times[i]

        if Sum < M:
            l = m + 1
        else:
            r = m

    print(f"#{T} {l}")

print(time.time() - st)





#
# import sys
# import time
# sys.stdin = open('../Input/3074.txt', 'r')
#
# st = time.time()
#
#
# TC = int(input())
# for T in range(1, TC+1):
#     N, M = map(int, input().split())
#
#     times = [0]*N
#     for i in range(N):
#         times[i] = int(input())
#
#     # binary search
#     r = min(times) * M
#     l = 1
#
#     while l < r:
#         m = (l + r) // 2
#
#         Sum = 0
#         for i in range(N):
#             Sum += m//times[i]
#
#         if Sum < M:
#             l = m + 1
#         else:
#             r = m
#
#     print(f"#{T} {l}")
#
# print(time.time() - st)





# for T in range(int(input())):
#     N, M = map(int, input().split())
#     # N: counters, M: passengers
#     time = [int(input()) for _ in range(N)]
#
#     # binary search
#     r = min(time) * M
#     l = 1
#
#     while l < r:
#         m = (l + r) // 2
#
#         Sum = 0
#         for i in range(N):
#             Sum += m//time[i]
#
#         if Sum < M:
#             l = m + 1
#         else:
#             r = m
#
#     print(f"#{T+1} {l}")






###########################################################################
# TIme Out

# def getMin(time, N, M, Min):
#     if Min > time[1]:
#         while 1:
#             Min -= 1
#             tmp = 1
#             pa = [Min//p for p in time]
#             Sum = 0
#             for i in range(N):
#                 if Sum > M:
#                     tmp = 0
#                     break
#                 Sum += pa[i]
#                 tmp = 1
#             if tmp and Sum < M:
#                 break
#         return Min
#     else:
#         return Min
#
#
# for T in range(int(input())):
#     N, M = map(int, input().split())
#     # N: counters, M: passengers
#     time = [int(input()) for _ in range(N)]
#     time.sort()
#
#     Min = time[0] * M
#
#     print(f"#{T+1} {getMin(time, N, M, Min)+1}")







