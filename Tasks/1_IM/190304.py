"""
1231. [S/W 문제해결 기본] 9일차 - 중위순회

== 완전 이진 트리 ==

"""

import sys
sys.stdin = open('../Input/input1231.txt', 'r')

def inorder(T):
    global tree, val
    if T:
        inorder(tree[T][0])
        print(val[T], end="")
        inorder(tree[T][1])

for T in range(1, 11):
    N = int(input())
    tmp = [input().split() for _ in range(N)]

    tree = [[0] * 2 for _ in range(N+1)]
    val = [0] * (N + 1)

    for x in tmp:
        idx, v = int(x[0]), x[1]
        val[idx] = v
        try:
            tree[idx][0] = int(x[2])
        except: pass
        try:
            tree[idx][1] = int(x[3])
        except: pass

    print("#{}".format(T), end=" ")
    inorder(1)
    print()





#####################################################

#
# for T in range(1, 11):
#     N = int(input())
#     tmp = [input().split() for _ in range(N)]
#
#     tree = [[] for _ in range(N + 1)]
#     val = [0] * (N + 1)
#     for x in tmp:
#         idx, v = int(x[0]), x[1]
#         val[idx] = v
#         try:
#             l = int(x[2])
#             tree[idx] += [l]
#         except:
#             pass
#         try:
#             r = int(x[3])
#             tree[idx] += [r]
#         except:
#             pass
#
#     curr = N
#     route = [val[curr]]
#     vis = [1] + [0] * N
#     vis[curr] = 1
#
#     while 0 in vis:
#         if not [x for x in tree[curr] if not vis[x]]:
#             while 1:
#                 curr = curr // 2
#                 if [x for x in tree[curr] if not vis[x]]:
#                     break
#         else:
#             for ch in [x for x in tree[curr] if not vis[x]]:
#                 route.append(val[ch])
#                 vis[ch] = 1
#
#     print("#{} {}".format(T, N))