

# from itertools import permutations, combinations
#
# a = [1, 1, 2, 3]
#
# print(*set(list(combinations(a, 4))), sep='\n')

a = '12345'

b = [int(x) for x in a]

print(b)



# import sys
# sys.stdin = open('../Input/5250.txt', 'r')
#
# INF = float('inf')
#
# # direction: 0up, 1right, 2down, 3left
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# def min_not_vis(vis, dis):
#     i, j = -1, -1
#     Min = INF
#     for coor in vis:
#         if dis[coor[0]][coor[1]] < Min:
#             Min = dis[coor[0]][coor[1]]
#             i, j = coor
#     return i, j
#
# TC = int(input())
# for T in range(1, TC+1):
#     N = int(input())
#     arr = [0]*N
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#     print(arr)
#
#     sel = [[0]*N for _ in range(N)]  # coordinates that have been visited at least once (dis != INF)
#     cnt = 0  # count of calculated coordinates == len(cal)
#     dis = [[INF]*N for _ in range(N)]
#
#     # start at top left corner
#     dis[0][0] = 0
#
#     while cnt <= N*N:
#         i, j = min_not_vis(vis, dis)   # row, col
#         vis.append((i, j))
#         cnt += 1
#         print(i, j)
#         for d in range(4):
#             r, c = i+dr[d], j+dc[d]
#             if 0 <= r < N and 0 <= c < N:
#                 dis[r][c] = dis[i][j] + 1 + max(0, arr[r][c]-arr[i][j])
#
#     print(f"#{T} {dis[N-1][N-1]}")


# def power_set_i():
#     bit = [0, 0, 0]
#     for i in range(2):
#         bit[0] = i
#         for j in range(2):
#             bit[1] = j
#             for k in range(2):
#                 bit[2] = k
#                 print(bit)
#
#
# def power_set_b():
#     arr = [1, 2, 3]
#     n = len(arr)
#     for i in range(1 << n):
#         print('{', end =' ')
#         for j in range(n+1):
#             if i & (1 << j):
#                 print(arr[j], end = ' ')
#         print('}')
#
#
# def power_set_r(k):
#     if k == N:
#         print(a)
#     else:
#         a[k] = 1
#         power_set_r(k + 1)
#         a[k] = 0
#         power_set_r(k + 1)
#
#
# print('부분집합 반복문')
# power_set_i()
#
# print('부분집합 바이너리 카운팅')
# power_set_b()
#
# N = 3
# a = [0] * N
# print('부분집합 재귀문')
# power_set_r(0)




# tmp = {}
# for num in range(10):
#     tmp[str(num)] = (bin(int(str(num), 16))[2:].zfill(4))
# for alpha in ['A', 'B', 'C', 'D', 'E', 'F']:
#     tmp[alpha] = (bin(int(alpha, 16))[2:].zfill(4))
#
# print(tmp)


# import sys
# sys.stdin = open('Input/tmp.txt', 'r')
#
#
# for T in range(int(input())):
#     b, c = input(), input()
#     lb, lc = len(b), len(c)
#     db, dc = int(b, 2), int(c, 3)
#
#     found = 0
#     for i in range(lb):
#         if b[i] == '1':
#             tb = db - 2**(lb-1-i)
#         else:
#             tb = db + 2**(lb-1-i)
#         for j in range(lc):
#             if c[j] == '0':
#                 tc1 = dc + 3**(lc-1-j)  # change to 1
#                 tc2 = dc + 2*(3**(lc-1-j))  # change to 2
#             elif c[j] == '1':
#                 tc1 = dc - 3**(lc-1-j)  # change to 0
#                 tc2 = dc + 3**(lc-1-j)  # change to 2
#             else:  # 2
#                 tc1 = dc - 2*(3**(lc-1-j))   # change to 0
#                 tc2 = dc - 3**(lc-1-j)  # change to 1
#             if tb == tc1 or tb == tc2:
#                 ans, found = tb, 1
#                 break
#         if found:
#             break
#
#     print(ans)
#









# def opp(n):
#     return '0' if n == '1' else '1'
#
# def opp3(c, j, p, q): # p, q: whatever is not c[j]
#
#
# for T in range(int(input())):
#     b, c = input(), input()  # 2진수, 3진수
#     print(f"[2진수]: {b} // [3진수]: {c}")
#
#     tmp = 0
#     for i in range(len(b)):
#         b2 = b[:i] + opp(b[i])
#         if i < len(b)-1:
#             b2 += b[i+1:]
#         b3 = int(b2, 2)
#         for j in range(len(c)):
#             if c[j] == '0':
#
#             elif c[j] == '1':
#
#
#             else:  # 2:
#
#
#
#             c2 = c[:j] + opp(c[j])
#             if j < len(c)-1:
#                 c2 += c[j+1:]
#             print(f"2진수: {b2}->{b3} // 3진수: {c2}->{int(c2, 3)}")
#     print("=====")
