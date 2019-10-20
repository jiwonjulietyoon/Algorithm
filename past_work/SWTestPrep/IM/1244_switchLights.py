"""
스위치 켜고 끄기


출력: 한 줄에 20개까지만

"""


def switch(a):
    return "1" if a == "0" else "0"

N = int(input())
lights = [None] + input().split()
M = int(input())  # number of students
turn = [list(map(int, input().split())) for _ in range(M)]

for x in turn:
    if x[0] == 1: # boys
        for i in range(x[1], N+1, x[1]):
            lights[i] = switch(lights[i])
    else: # girls
        lights[x[1]] = switch(lights[x[1]])
        g = 0
        while x[1]+g+1 <= N and lights[x[1]-g-1] == lights[x[1]+g+1]:
            lights[x[1]-g-1] = switch(lights[x[1]-g-1])
            lights[x[1]+g+1] = switch(lights[x[1]+g+1])
            g += 1

for i in range(1, N+1):
    print(lights[i], end=" ")
    if not i % 20:
        print()





##################################################################
# Runtime Error

# def switch(a):
#     return "1" if a == "0" else "0"
#
# N = int(input())
# lights = [None] + input().split()
# M = int(input())  # number of students
# turn = [list(map(int, input().split())) for _ in range(M)]
#
# for x in turn:
#     if x[0] == 1: # boys
#         for i in range(x[1], N+1, x[1]):
#             lights[i] = switch(lights[i])
#     else: # girls
#         g = 0
#         while lights[x[1]-g-1] == lights[x[1]+g+1]:
#             g += 1
#         for i in range(x[1]-g, x[1]+g+1):
#             lights[i] = switch(lights[i])
#
# for i in range(1, N+1):
#     print(lights[i], end=" ")
#     if i == 20:
#         print()