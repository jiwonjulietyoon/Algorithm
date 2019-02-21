# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

"""
"""






import sys
sys.stdin = open('input4881.txt', 'r')



def is_attack(i, j):
    # checking if there is a queen in row or column
    global idx, N
    for k in range(N):
        if idx[i][k]==1 or idx[k][j]==1:
            return True
    # checking diagonals
    for k in range(N):
        for l in range(N):
            if (k+l==i+j) or (k-l==i-j):
                if idx[k][l]==1:
                    return True
    return False

def min_sum(arr, N, Sum):
    global Min, idx
    if Sum > Min:
        return
    if N == 0:
        return True
    for i in range(N):
        for j in range(N):
            if not is_attack(i, j) and not idx[i][j]:
                idx[i][j] = 1
                Sum += arr[i][j]
                if min_sum(arr, N-1, Sum):
                    return True
                idx[i][j] = 0
                # Sum -= arr[i][j]
    return False

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [ [0]*N for _ in range(N) ]
    # selected = [0] * N
    Min = 100
    min_sum(arr, N, 0)
    print(f"#{T + 1} {Min}")


#############################################################################

# def min_sum(arr, selected, Sum, k):
#     global Min
#     N = len(arr)
#     if Sum > Min:  # if sum of elements added so far already exceeds the record minimum, quit.
#         return
#     if k == N:
#         if Sum < Min:
#             Min = Sum
#         return
#     for i in range(N):
#         print('-----')
#         for j in range(N):
#             if not selected[j]:
#                 selected[j] = 1
#                 Sum += arr[i][j]
#                 print(arr[i][j], Sum, selected)
#                 if min_sum(arr, selected, Sum, k+1):
#                     return True
#                 selected[j] = 0
#     return False
#
#
# for T in range(int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     selected = [0] * N
#     Min = 100
#     min_sum(arr, selected, 0, 0)
#     print(f"#{T + 1} {Min}")













###############################################################################


# arr : 2D List
# selected : record of selected indexes from each column
# Sum : sum of elements selected from each column
# N : arr size


def min_sum(arr, selected, Sum, N):
    global Min
    if Sum > Min:  # if sum of elements added so far already exceeds the record minimum, quit.
        return
    if N == 0:
        return True
    for i in range(N):
        for j in range(N):
            if not selected[j]:
                Sum += arr[i][j]
                selected[j] = 1
                if min_sum(arr, selected, Sum, N-1):
                    return True
                selected[j] = 0
        if Sum < Min:
            Min = Sum
    return False


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 100
    selected = [0] * N
    min_sum(arr, selected, 0, N)
    print(f"#{T + 1} {Min}")














##################################################################
######### 코드는 문제 없는 것 같으나, 시간 제한 초과로 인해 오답처리 (7/10 correct)

def permute(a, l, r, arr):
    global sums, Min
    if l == r:
        tmp = 0
        for i in range(len(a)):
            tmp += arr[i][a[i]]
            if tmp > Min:
                continue
        if tmp < Min:
            Min = tmp
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, arr)
            a[l], a[i] = a[i], a[l]

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 100
    permute(list(range(N)), 0, N-1, arr)
    print(f"#{T + 1} {Min}")



##################################################################
######### 코드는 문제 없는 것 같으나, 시간 제한 초과로 인해 오답처리 (6/10 correct)

def permute(a, l, r, arr):
    global sums, Min
    if l == r:
        tmp = sum([arr[i][a[i]] for i in range(len(a))])
        if tmp < Min:
            Min = tmp
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, arr)
            a[l], a[i] = a[i], a[l]

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 100
    permute(list(range(N)), 0, N-1, arr)
    print(f"#{T + 1} {Min}")










##########################################################################
##########################################################################
##########################################################################


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    idx = [0] * N    # record selected columns (index number)
    sel = [0] * N    # record selected numbers from each row

    for r in range(N): # for each row
        sel[r] = min(arr[r])  # select the minimum
        idx[r] = arr[r].index(sel[r])  # and record its index

    while(1):
        if len(set(idx)) == N:
            break
        else:  # if there are any redundant index numbers
         

    print(f"#{T+1} {ans}")




########################################################################

"""
[
    [(1, 1), (0, 2), (2, 2)], 
    [(0, 5), (2, 5), (1, 8)], 
    [(1, 2), (2, 2), (0, 7)]
]

Try all elements of each row, starting from the bottom row




"""





