

# unfinished


""" 자동차경주대회

- 정비소에서 정비하는 데에 걸리는 시간들의 합을 가장 적게

- backtracking and pruning?

"""

import sys
sys.stdin = open('../Input/2651.txt', 'r')



def backtrack(c, Sum, route):  # c: current position , Sum: time spent so far,  st: stops stopped by
    global Min, stops, N, dis, time
    if sum(btw[c+1:]) <= dis:
        if Sum < Min:
            Min = Sum
            stops = route[:]
    else:
        tmp = 0
        st = []
        for i in range(c+1, N+1):
            if tmp + btw[i] <= dis:
                st.append(i)
                tmp += btw[i]
            else:
                break
        for x in st:
            c = x
            Sum += time[c]
            route.append(c)
            if Sum > Min:
                return
            backtrack(c, Sum, route)
            Sum -= time[x]
            c = route.pop()


dis = int(input())  # 한번에 갈 수 있는 최대 거리
N = int(input())  # number of stops
btw = [0] + list(map(int, input().split()))  # distance in between stops
time = [0] + list(map(int, input().split()))  # time needed at each stop

Min = sum(time)   # record minimum time spent at stops
stops = []        # record stops visited

if dis >= sum(btw):  # no need to stop
    print(0)
else:
    backtrack(0, 0, [])
    print(Min)
    print(len(stops))
    print(*stops, sep=" ")












#####################################################################
# 시간 초과


# def backtrack(c, Sum, route):  # c: current position , Sum: time spent so far,  st: stops stopped by
#     global Min, stops, N, dis, time
#     if sum(btw[c+1:]) <= dis:
#         if Sum < Min:
#             Min = Sum
#             stops = route[:]
#     else:
#         tmp = 0
#         st = []
#         for i in range(c+1, N+1):
#             if tmp + btw[i] <= dis:
#                 st.append(i)
#                 tmp += btw[i]
#             else:
#                 break
#         for x in st:
#             c = x
#             Sum += time[c]
#             route.append(c)
#             if Sum > Min:
#                 return
#             backtrack(c, Sum, route)
#             Sum -= time[x]
#             c = route.pop()
# 
# 
# dis = int(input())  # 한번에 갈 수 있는 최대 거리
# N = int(input())  # number of stops
# btw = [0] + list(map(int, input().split()))  # distance in between stops
# time = [0] + list(map(int, input().split()))  # time needed at each stop
# 
# Min = sum(time)   # record minimum time spent at stops
# stops = []        # record stops visited
# 
# if dis >= sum(btw):  # no need to stop
#     print(0)
# else:
#     backtrack(0, 0, [])
#     print(Min)
#     print(len(stops))
#     print(*stops, sep=" ")


"""
1. 현재 지점에서, dis 내의 거리에 있는 정비소를 tmp에 담는다.
2. tmp를 for loop 돌면서, backtracking 함수에 돌린다


"""



