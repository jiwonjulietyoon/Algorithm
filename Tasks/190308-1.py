# 6109. 추억의 2048게임

import sys
sys.stdin = open('../Input/input6109.txt', 'r')

def arr_reader(arr, N, d):
    new = [[] for _ in range(N)]
    for i in range(N):
        z = []
        for j in range(N):
            if d == "left" or d == "right":
                if arr[i][j]:
                    new[i].append(arr[i][j])
                else:
                    z.append(0)
            elif d == "up" or d == "down":
                if arr[j][i]:
                    new[i].append(arr[j][i])
                else:
                    z.append(0)
        if d == "right" or d == "down":
            new[i].reverse()
        new[i] += z
    return new

def swipe(arr, N):
    for row in arr:
        for i in range(1, N):
            if row[i] == row[i-1]:
                row[i-1] *= 2
                row.pop(i)
                row.append(0)
            if row[i] == 0:
                break
    return arr

def arr_writer(arr, N, d):
    final = [[0]*N for _ in range(N)]
    if d == "up":
        for i in range(N):
            for j in range(N):
                final[i][j] = arr[j][i]
    elif d == "down":
        for i in range(N):
            for j in range(N):
                final[i][j] = arr[j][N-1-i]
    elif d == "left":
        return arr
    elif d == "right":
        for i in range(N):
            for j in range(N):
                final[i][j] = arr[i][N-1-j]
    return final

for T in range(int(input())):
    N, d = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    print("#{}".format(T+1))

    if N == 1:
        print(arr[0][0])
    else:
        read = arr_reader(arr, N, d)
        res = swipe(read, N)
        for x in arr_writer(res, N, d):
            print(*x, sep=" ")



