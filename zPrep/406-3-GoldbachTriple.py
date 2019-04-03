
import sys
sys.stdin = open('Input/406-3_1.txt', 'r')
# sys.stdin = open('Input/tmp.txt', 'r')

"""
백준 https://www.acmicpc.net/contest/problem/406/3

C번 - 골드바흐 트리플

"""

num = [0, 0] + [1] * 999999
pnidx = [0]*1000001
pn = []
PN = 0  # number of prime numbers
for i in range(2, 1000001):
    if num[i]:
        pn.append(i)
        pnidx[i] = 1
        PN += 1
        for j in range(i*2, 1000001, i):
            num[j] = 0



TC = int(input())
ans = [0]*TC

for T in range(999997, 1000001, 2):
    N = T
    ans = 0
    # ans[T]: total number of unique Goldbach Triples
    if pnidx[N-4]:   # 2 + 2 + []
        ans = 1

    # start idx: 1 (start with prime number 3)
    for i in range(1, PN):
        if pn[i] > N-6:
            break
        for j in range(i, PN):
            two = pn[i]+pn[j]
            if two > N-3:
                break
            if N-two >= pn[j] and pnidx[N-two]:
                ans += 1
    print(N, ans)




#############################################
# faster, but still too slow


num = [0, 0] + [1] * 999999
pnidx = [0]*1000001
pn = []
PN = 0  # number of prime numbers
for i in range(2, 1000001):
    if num[i]:
        pn.append(i)
        pnidx[i] = 1
        PN += 1
        for j in range(i*2, 1000001, i):
            num[j] = 0



TC = int(input())
ans = [0]*TC

for T in range(TC):
    N = int(input())

    # ans[T]: total number of unique Goldbach Triples
    if pnidx[N-4]:   # 2 + 2 + []
        ans[T] = 1

    # start idx: 1 (start with prime number 3)
    for i in range(1, PN):
        if pn[i] > N-6:
            break
        for j in range(i, PN):
            two = pn[i]+pn[j]
            if two > N-3:
                break
            if N-two >= pn[j] and pnidx[N-two]:
                ans[T] += 1


print(*ans, sep="\n")







######################################################
# too slow

# pn = []
# num = [0, 0] + [1] * 999999
# for i in range(2, 1000001):
#     if num[i]:
#         pn.append(i)
#         for j in range(i*2, 1000001, i):
#             num[j] = 0
# PN = len(pn)
#
# TC = int(input())
# ans = [0]*TC
#
# for T in range(TC):
#     N = int(input())
#
#     # ans[T]: total number of unique Goldbach Triples
#     if N-4 in pn:   # 2 + 2 + []
#         ans[T] = 1
#
#     # start idx: 1 (start with prime number 3)
#     for i in range(1, PN):
#         if pn[i] > N-6:
#             break
#         for j in range(i, PN):
#             if pn[i]+pn[j] > N-3:
#                 break
#             for k in range(j, PN):
#                 if pn[i]+pn[j]+pn[k] == N:
#                     ans[T] += 1
#                     break
#
# print(*ans, sep="\n")


