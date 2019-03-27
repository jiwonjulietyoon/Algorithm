
# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

# Time out!


import sys
sys.stdin = open('../Input/5204.txt', 'r')


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    ll, lr = len(left), len(right)
    res = [0] * (ll + lr)
    l = r = i = 0  # idx
    while l < ll and r < lr:  # while both lists each have at least 1 element
        # compare each of the first elements; append smaller element to [result]
        if left[l] <= right[r]:
            res[i] = left[l]
            l += 1
        else:
            res[i] = right[r]
            r += 1
        i += 1

    if l < ll:  # if [left] has remaining elements
        res[i:] = left[l:]
    if r < lr:  # if [right] has remaining elements
        res[i:] = right[r:]
    return res


def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. DIVIDE
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # Recursive -> until each sub-list only has 1 element each
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER : merge the divided lists
    return merge(left, right)


for T in range(int(input())):
    N = int(input())
    m = list(map(int, input().split()))
    cnt = 0
    print(f"#{T + 1} {merge_sort(m)[N//2]} {cnt}")


############################################################################
# TIme out 2

# def merge(left, right):
#     global cnt
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     ll, lr = len(left), len(right)
#     res = [0]*(ll+lr)
#     l = r = i = 0  # idx
#     while l < ll and r < lr:  # while both lists each have at least 1 element
#         # compare each of the first elements; append smaller element to [result]
#         if left[l] <= right[r]:
#             res[i] = left[l]
#             l += 1
#         else:
#             res[i] = right[r]
#             r += 1
#         i += 1
#
#     if l < ll:  # if [left] has remaining elements
#         res[i:] = left[l:]
#     if r < lr:  # if [right] has remaining elements
#         res[i:] = right[r:]
#     return res
#
#
# def merge_sort(m):
#     if len(m) <= 1:
#         return m
#
#     # 1. DIVIDE
#     mid = len(m) // 2
#     left = m[:mid]
#     right = m[mid:]
#
#     # Recursive -> until each sub-list only has 1 element each
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     # 2. CONQUER : merge the divided lists
#     return merge(left, right)
#
#
# for T in range(int(input())):
#     N = int(input())
#     m = list(map(int, input().split()))
#     cnt = 0
#     print(f"#{T+1} {merge_sort(m)[N//2]} {cnt}")







##################################################################
# Time Out


# def merge(left, right):
#     global cnt
#     if left[-1] > right[-1]:
#         cnt += 1
#     result = []
#     while len(left) and len(right):  # while both lists have at least 1 element
#         # compare each of the first elements; append smaller element to [result]
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#
#     if len(left) > 0:  # if [left] has a remaining element
#         result.extend(left)
#     if len(right) > 0:  # if [right] has a remaining element
#         result.extend(right)
#     return result
#
#
# def merge_sort(m):
#     if len(m) <= 1:
#         return m
#
#     # 1. DIVIDE
#     mid = len(m) // 2
#     left = m[:mid]
#     right = m[mid:]
#
#     # Recursive -> until each sub-list only has 1 element each
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     # 2. CONQUER : merge the divided lists
#     return merge(left, right)
#
#
# for T in range(int(input())):
#     N = int(input())
#     m = list(map(int, input().split()))
#     cnt = 0
#     print(f"#{T+1} {merge_sort(m)[N//2]} {cnt}")
