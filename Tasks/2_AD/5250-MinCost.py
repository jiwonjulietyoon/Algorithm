
# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

import sys
sys.stdin = open('../Input/5250.txt', 'r')






"""
2nd try

time over

Note: can also move up or left

"""

# def solve(r, c, Sum):
#     global arr, N, Min
#     if Sum > Min:
#         return
#     if r == N-1 and c == N-1:
#         if Sum < Min:
#             Min = Sum
#     elif r == N-1:
#         solve(r, c+1, Sum+max(0, arr[r][c+1]-arr[r][c]))
#     elif c == N-1:
#         solve(r+1, c, Sum+max(0, arr[r+1][c]-arr[r][c]))
#     else:
#         # go right
#         solve(r, c+1, Sum+max(0, arr[r][c+1]-arr[r][c]))
#         # go down
#         solve(r+1, c, Sum+max(0, arr[r+1][c]-arr[r][c]))
#
#
# TC = int(input())
# for T in range(1, TC+1):
#     N = int(input())
#     arr = [0]*N
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#
#     Min = 2*N-2
#     for i in range(N-1):
#         Min += (max(0, arr[i+1][0]-arr[i][0]) + max(0, arr[N-1][i+1]-arr[N-1][i]))
#
#     solve(0, 0, 2*N-2)
#
#     print(f"#{T} {Min}")




"""
first try

Time Over

"""

#
# def solve(r, c, Sum):
#     global arr, N, Min
#     if Sum > Min:
#         return
#     if r == N-1 and c == N-1:
#         if Sum < Min:
#             Min = Sum
#     elif r == N-1:
#         if arr[r][c] < arr[r][c+1]:
#             solve(r, c+1, Sum+arr[r][c+1]-arr[r][c])
#         else:
#             solve(r, c+1, Sum)
#     elif c == N-1:
#         if arr[r][c] < arr[r+1][c]:
#             solve(r+1, c, Sum+arr[r+1][c]-arr[r][c])
#         else:
#             solve(r+1, c, Sum)
#     else:
#         # go right
#         if arr[r][c] < arr[r][c+1]:
#             s = Sum+arr[r][c+1]-arr[r][c]
#         else:
#             s = Sum
#         solve(r, c+1, s)
#         # go down
#         if arr[r][c] < arr[r + 1][c]:
#             s = Sum+arr[r+1][c]-arr[r][c]
#         else:
#             s = Sum
#         solve(r+1, c, s)
#
#
# TC = int(input())
# for T in range(1, TC+1):
#     N = int(input())
#     arr = [0]*N
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#
#     Min = 2*N-2
#     for i in range(N-1):
#         if arr[i][0] < arr[i+1][0]:
#             Min += arr[i+1][0]-arr[i][0]
#         if arr[N-1][i] < arr[N-1][i+1]:
#             Min += arr[N-1][i+1] - arr[N-1][i]
#
#     solve(0, 0, 2*N-2)
#
#     print(f"#{T} {Min}")