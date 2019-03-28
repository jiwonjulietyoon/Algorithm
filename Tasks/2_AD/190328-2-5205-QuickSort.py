# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

import sys
sys.stdin = open('../Input/5205.txt', 'r')


def partition(arr, l, r):  # l: idx of leftmost element  // r: idx of rightmost element
    i = l-1  # idx of smaller element
    p = arr[r]  # pivot: last element

    for j in range(l, r):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1


def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)


for T in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    quickSort(num, 0, N-1)
    print(f"#{T+1} {num[N//2]}")


