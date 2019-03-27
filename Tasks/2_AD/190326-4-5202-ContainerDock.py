# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

import sys
sys.stdin = open('../Input/5202.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')

"""


"""


def check(slot, hours): # return boolean
    for i in range(slot[0], slot[1]):
        if i not in hours:
            return 0
    return 1

for T in range(int(input())):
    N = int(input())
    slots = [list(map(int, input().split())) for _ in range(N)]
    slots.sort(key=lambda x: x[1]-x[0])

    cnt = 0
    hours = list(range(24))
    for slot in slots:
        if check(slot, hours):
            for i in range(slot[0], slot[1]):
                hours.remove(i)
            cnt += 1

    print(f"#{T+1} {cnt}")















#################################################
# 제한 시간 초과: subsets

# def check(sub):
#     global Max
#     n = len(sub)
#     if n <= Max:
#         return 0
#     for i in range(n-1):
#         if sub[i][1] > sub[i+1][0]:
#             return 0
#     Max = n
#     return 1
#
#
# for T in range(int(input())):
#     N = int(input())
#     time = [list(map(int, input().split())) for _ in range(N)]
#     time.sort()
#     Max = 0
#
#     for i in range((1<<N)-1, -1, -1):
#         sub = []
#         for j in range(N):
#             if i & (1<<j):
#                 sub.append(time[j])
#         if check(sub):
#             break
#
#     print(f"#{T+1} {Max}")

