# 1865. 동철이의 일 분배

import sys
sys.stdin = open('../Input/1865.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')



def solve(k, prod):
    global N, arr, vis, Max
    if prod <= Max:
        return
    if k == N:
        if prod > Max:
            Max = prod
    else:
        for i in range(N):
            if not vis[i]:
                vis[i] = 1
                solve(k+1, prod * arr[k][i]/100)
                vis[i] = 0

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    vis = [0] * N
    Max = 0

    solve(0, 1)
    print("#%d %.6f" % (T+1, Max*100))






# def solve(k, Sum, num):
#     global arr, N, Max, vis
#     if k == N:
#         if Sum > Max:
#             Max = Sum
#             Maxnum = num[:]
#     else:
#         for i in range(N):
#             if not vis[i]:
#                 vis[i] = 1
#                 num[k] = arr[k][i]
#                 # print(num)
#                 solve(k+1, Sum+arr[k][i], num)
#                 vis[i] = 0
#                 num[k] = 0
#
#
#
# for T in range(int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     vis = [0] * N
#     Max = 0
#     Maxnum = []
#
#     solve(0, 0, [0]*N)
#     print(Max)
#     print(Maxnum)



#
# def solve(k, num):
#     global arr, N, collection, vis
#     if k == N:
#         collection.append(num)
#     else:
#         for i in range(N):
#             if not vis[i]:
#                 vis[i] = 1
#                 num.append(arr[k][i])
#                 k += 1
#                 print(num)
#                 solve(k, num)
#                 k -= 1
#                 num.remove(arr[k][i])
#                 vis[i] = 0
#
#
#
# for T in range(int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     vis = [0] * N
#     collection = []
#
#     solve(0, [])
#     print(collection)
#     # print(Max)
