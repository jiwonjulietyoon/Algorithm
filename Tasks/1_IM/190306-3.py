# 2805. 농작물 수확하기

import sys
sys.stdin = open('../Input/input2805.txt', 'r')

for T in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]

    Sum = 0
    mid = N//2

    for i in range(mid):  # exclude middle row
        Sum += sum(map(int, list(arr[i][mid-i:mid+i+1])))  # top
        Sum += sum(map(int, list(arr[N-1-i][mid-i:mid+i+1])))  # bottom

    Sum += sum(map(int, list(arr[mid])))  # middle row

    print("#{} {}".format(T+1, Sum))