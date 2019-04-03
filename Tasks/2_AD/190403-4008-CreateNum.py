# 4008. [모의 SW 역량테스트] 숫자 만들기

import sys
sys.stdin = open('../Input/4008.txt', 'r')

def DFS(res, i, a, s, m, d):
    global Max, Min, N
    if i == N-1:
        if res < Min:
            Min = res
        if res > Max:
            Max = res
    else:
        if a:
            DFS(res+num[i+1], i+1, a-1, s, m, d)
        if s:
            DFS(res-num[i+1], i+1, a, s-1, m, d)
        if m:
            DFS(res*num[i+1], i+1, a, s, m-1, d)
        if d:
            DFS(int(res/num[i+1]), i+1, a, s, m, d-1)

for T in range(1, int(input())+1):
    N = int(input())
    a, s, m, d = map(int, input().split())  # add, subtract, multiply, divide
    num = list(map(int, input().split()))

    Min = 100000001
    Max = -100000001
    DFS(num[0], 0, a, s, m, d)

    print(f"#{T} {Max-Min}")











# def DFS(i, tmp, a, b, c, d):
#     if not a and not b and not c and not d:
#         global Max, Min
#         if Min == None:
#             Min = Max = tmp
#         if tmp < Min:
#             Min = tmp
#         elif tmp > Max:
#             Max = tmp
#         return
#     if a:
#         DFS(i+1, tmp+nums[i+1], a-1, b, c, d)
#     if b:
#         DFS(i+1, tmp-nums[i+1], a, b-1, c, d)
#     if c:
#         DFS(i+1, tmp*nums[i+1], a, b, c-1, d)
#     if d:
#         DFS(i+1, int(tmp/nums[i+1]), a, b, c, d-1)
#
#
# for T in range(1, int(input()) + 1):
#     N = int(input())
#     a, b, c, d = map(int, input().split())
#     nums = list(map(int, input().split()))
#     Min = Max = None
#     DFS(0, nums[0], a, b, c, d)
#     print('#{} {}'.format(T, Max-Min))


"""
제한 시간 초과
- used itertools.permutations
"""

#
# def cal(a, op, b):
#     if op == 1:
#         return a+b
#     elif op == 2:
#         return a-b
#     elif op == 3:
#         return a*b
#     elif op == 4:
#         return int(a/b)
#
# TC = int(input())
# for T in range(1, TC+1):
#     N = int(input())  # N integers given
#     tmp = list(map(int, input().split()))
#     ops = []
#     for i in range(4):
#         ops.extend([i+1]*tmp[i])
#
#     nums = list(map(int, input().split()))
#     perm = set(permutations(ops, N-1))
#
#     Min = 100000001
#     Max = -100000001
#
#     for p in perm:
#         res = nums[0]
#         for i in range(N-1):
#             res = cal(res, p[i], nums[i+1])
#         if res < Min:
#             Min = res
#         if res > Max:
#             Max = res
#
#     print(f"#{T} {Max-Min}")



