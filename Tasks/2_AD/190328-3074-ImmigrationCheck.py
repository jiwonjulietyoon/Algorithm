# 3074. 입국심사


# Not finished

import sys
sys.stdin = open('../Input/3074.txt', 'r')



def getIdx(time, N, M):
    t = time[-1]
    if sum([t//p for p in time]) < M:
        return N
    else:
        for i in range(N-2, -1, -1):
            t = time[i]
            if sum([t//time[j] for j in range(i+1)]) < M:
                return i+2



for T in range(int(input())):
    N, M = map(int, input().split())
    # N: counters, M: passengers
    time = [int(input()) for _ in range(N)]
    time.sort()

    print(time)

    # print(getIdx(time, N, M))
    time = time[:getIdx(time, N, M)]

    print(time)




    # for i in range(N):
    #     t = time[i]
    #     pa = [t//time[j] for j in range(N-1, i-1, -1)]
    #     if sum(pa) <= M:
    #         break
    #
    # print(i)





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







