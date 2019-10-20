import sys
sys.stdin = open('Input/2115.txt', 'r')
# sys.stdin = open('Input/tmp.txt', 'r')

"""
2115. [모의 SW 역량테스트] 벌꿀채취

"""

def calc_sum(r, c, sub, a, k, Sum, profit):
    global res
    if Sum > C:
        return
    if k == M:
        if Sum <= C:
            if profit > res[r][c]:
                res[r][c] = profit
    else:
        a[k] = 1
        calc_sum(r, c, sub, a, k+1, Sum+sub[k], profit+sub[k]**2)
        a[k] = 0
        calc_sum(r, c, sub, a, k+1, Sum, profit)

def get_sum(r, c, sub):
    global res
    if res[r][c]:
        return res[r][c]
    else:
        calc_sum(r, c, sub, [0]*M, 0, 0, 0)
        return res[r][c]

for T in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    res = [[0]*(N-M+1) for _ in range(N)]  # memoization
    Max = 0  # max sum of both M's

    for i in range(N):
        for j in range(N-M+1):
            for p in range(i, N):
                if i == p:  # in same row:
                    for q in range(j+M, N-M+1):
                        s = get_sum(i, j, arr[i][j:j+M]) + get_sum(p, q, arr[p][q:q+M])
                        if s > Max:
                            Max = s
                else:
                    for q in range(N-M+1):
                        s = get_sum(i, j, arr[i][j:j+M]) + get_sum(p, q, arr[p][q:q+M])
                        if s > Max:
                            Max = s

    print(f"#{T} {Max}")










##################################################
# incorrect



# def honey(sub, a, k, Sum, profit):
#     global Max
#     if Sum > C:
#         return
#     if k == M:
#         if Sum <= C:
#             for i in range(2):
#                 if profit > Max[i]:
#                     Max[i] = profit
#                     Max.sort()
#                     break
#     else:
#         a[k] = 1
#         honey(sub, a, k + 1, Sum + sub[k], profit + sub[k] ** 2)
#         a[k] = 0
#         honey(sub, a, k + 1, Sum, profit)
#
#
# for T in range(1, int(input()) + 1):
#     N, M, C = map(int, input().split())
#     arr = [0] * N
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#     print(*arr, sep="\n")
#
#     Max = [0, 0]
#
#     if M * 2 < N:  # if two M's don't fit into a single row
#
#     # for i in range(N):  # for each row
#     #     for j in range(0, N-M+1, M):  # for each sub-row
#     #         sub = arr[i][j:j+M]
#     #         honey(sub, [0]*M, 0, 0, 0)
#
#     print(Max)
#     print(f"#{T} {sum(Max)}")

