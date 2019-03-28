# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

import sys
sys.stdin = open('../Input/5207.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')

"""
Test Case 답이 틀렸음: should be #1 2 / #2 0 / #3 3

cnt 안 되는 경우:
- select left, left consecutively
- select right, right consecutively

- all else counts (including cases where target number is right at the middle of the list)

"""


def binary(List, l, r, n, left, right):
    global cnt, N
    if r >= l:
        m = (l+r) // 2
        if List[m] == n:
            cnt += 1
            return
        elif m > 0 and List[l] <= n <= List[m-1]:
            if left:
                return 0
            binary(List, l, m - 1, n, 1, 0)
        elif m < N-1 and List[m+1] <= n <= List[r]:
            if right:
                return 0
            binary(List, m+1, r, n, 0, 1)
        else:
            return 0
    else:
        return 0


for T in range(int(input())):
    N, M = map(int, input().split())   # N: len(A)  // M: len(B)
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    # check if elements in B are also in A

    cnt = 0
    for b in B:
        binary(A, 0, N-1, b, 0, 0)

    print(f"#{T+1} {cnt}")




