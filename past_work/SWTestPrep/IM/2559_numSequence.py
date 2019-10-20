
# 수열

import sys
sys.stdin = open('../Input/2559.txt', 'r')

N, K = map(int, input().split())
temp = list(map(int, input().split()))

Max = Sum = sum(temp[:K])  # initial sum

for i in range(1, N-K+1):
    Sum = Sum-temp[i-1]+temp[i+K-1]
    if Sum > Max:
        Max = Sum

print(Max)





#################################################
# 시간 초과

# N, K = map(int, input().split())
# temp = list(map(int, input().split()))
#
# Max = 0
#
# for i in range(0, N-K+1):
#     Sum = sum(temp[i:i+K])
#     if Sum > Max:
#         Max = Sum
#
# print(Max)
