import sys
# sys.stdin = open('Input/2117.txt', 'r')
sys.stdin = open('Input/tmp.txt', 'r')

""" 2117. [모의 SW 역량테스트] 홈 방범 서비스

Maximum number of houses covered; no loss

"""

cost_k = [0] + [k*k+(k-1)*(k-1) for k in range(1, 30)]
print("cost_k:", cost_k)
print()

def count(i, j, K):
    global Max





for T in range(1, int(input())+1):
    print("=> Test Case", T)
    N, M = map(int, input().split())

    tot = 0  # total number of houses
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        tot += sum(arr[i])
    print(*arr, sep="\n")
    print("total # of houses:", tot)
    print("Max total payment available:", tot*M)

    for e in range(30):
        if cost_k[e] > tot*M:
            break
    print("Max K:", e-1)

    Max = 1
    for K in range(e-1, 1, -1):
        for i in range(N):
            for j in range(N):
                count(i, j, K)



















#####################################################################################

# still incorrect


#
# cost_k = [0]+[k*k+(k-1)*(k-1) for k in range(1, 40)]
# # print(cost_k)
# # print()
#
# def count_house(i, j, K):
#     global Max
#     Sum = sum(arr[i][max(j-(K-1), 0):min(j+(K-1), N-1)+1])
#     # print("Sum:", Sum)
#     for a in range(1, K):
#         r_top, r_bot = i-a, i+a
#         if r_top >= 0:
#             Sum += sum(arr[r_top][max(j-(K-a-1), 0):min(j+(K-a-1), N-1)+1])
#         if r_bot <= N-1:
#             Sum += sum(arr[r_bot][max(j-(K-a-1), 0):min(j+(K-a-1), N-1)+1])
#     # print(K, Sum, lim[K], i, j)
#     if Sum >= lim[K]:
#         if Sum > Max:
#             Max = Sum
#
#
# for T in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [0]*N
#     tot = 0  # total number of houses in arr
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#         tot += sum(arr[i])
#     Max = 1  # at least one house
#     lim = [cost//M+1 for cost in cost_k]  # min number of houses needed for each size(k)
#
#     # print("total # of houses:", tot)
#     # print("lim:", lim)
#
#     for e in range(2, 40):
#         if tot < lim[e]:
#             break
#     # print(e-1)
#
#     flag = 0
#
#     for K in range(e-1, 1, -1): # start from e-1 (max end)
#         for i in range(N):
#             for j in range(N):
#                 count_house(i, j, K)  # arr[i][j] as the center
#                 if Max == cost_k[K]:
#                     flag = 1
#                     break
#             if flag:
#                 break
#         if flag:
#             break
#
#     print(f"#{T} {Max}")







###################################################################################
# 47/50 correct

# cost_k = [0]+[k*k+(k-1)*(k-1) for k in range(1, 30)]
# # print(cost_k)
# # print()
#
# def count_house(i, j, K):
#     global Max, stop
#     Sum = sum(arr[i][max(j-(K-1), 0):min(j+(K-1), N-1)+1])
#     # print("Sum:", Sum)
#     for a in range(1, K):
#         r_top, r_bot = i-a, i+a
#         if r_top >= 0:
#             Sum += sum(arr[r_top][max(j-(K-a-1), 0):min(j+(K-a-1), N-1)+1])
#         if r_bot <= N-1:
#             Sum += sum(arr[r_bot][max(j-(K-a-1), 0):min(j+(K-a-1), N-1)+1])
#     # print(K, Sum, lim[K], i, j)
#     if Sum >= lim[K]:
#         stop = 1
#         if Sum > Max:
#             Max = Sum
#
#
# for T in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [0]*N
#     tot = 0  # total number of houses in arr
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#         tot += sum(arr[i])
#     Max = 1  # at least one house
#     lim = [cost//M+1 for cost in cost_k]  # min number of houses needed for each size(k)
#
#     # print("total # of houses:", tot)
#     # print("lim:", lim)
#
#     for e in range(2, 30):
#         if tot < lim[e]:
#             break
#     # print(e-1)
#
#
#
#     flag = stop = 0
#
#
#
#     for K in range(e-1, 1, -1): # start from e-1 (max end)
#         for i in range(N):
#             for j in range(N):
#                 count_house(i, j, K)  # arr[i][j] as the center
#                 if Max == cost_k[K]:
#                     flag = 1
#                     break
#             if flag:
#                 break
#         if stop or flag:
#             break
#
#     print(f"#{T} {Max}")


