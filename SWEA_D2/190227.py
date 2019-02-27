# 1961. 숫자 배열 회전


import sys
sys.stdin = open('input1961.txt', 'r')


for T in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 90 deg
    arr90 = []
    for x in range(N):
        tmp = ""
        for y in range(N-1, -1, -1):
            tmp += str(arr[y][x])
        arr90.append(tmp)

    # 180 deg
    arr180 = []
    for y in range(N-1, -1, -1):
        tmp = ""
        for x in range(N-1, -1, -1):
            tmp += str(arr[y][x])
        arr180.append(tmp)

    # 270 deg
    arr270 = []
    for x in range(N-1, -1, -1):
        tmp = ""
        for y in range(N):
            tmp += str(arr[y][x])
        arr270.append(tmp)

    print(f"#{T+1}")
    for i in range(N):
        print(f"{arr90[i]} {arr180[i]} {arr270[i]}")