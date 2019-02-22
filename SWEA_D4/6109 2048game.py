
# 6109. 추억의 2048게임


"""
arr = [
    [4, 8, 2, 4, 0],
    [4, 4, 2, 0, 8],
    [8, 0, 2, 4, 4],
    [2, 2, 2, 2, 8],
    [0, 2, 2, 0, 0]
]

"""




def swipe(arr, N):
    for row in arr:
        i = 0
        while(1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row.pop(i+1)
                row.append(0)
            i += 1
            if row[i] == 0:
                break
    return arr


def arr_reader(arr, N, d):
    newarr = [[] for _ in range(N)]
    for i in range(N):
        tmp = []
        for j in range(N):
            if d == "left" or d == "right":
                if arr[i][j]:
                    newarr[i].append(arr[i][j])
                else:
                    tmp.append(0)
            elif d == "up" or d == "down":
                if arr[j][i]:
                    newarr[i].append(arr[j][i])
                else:
                    tmp.append(0)
        if d == "right" or d == "down":
            newarr[i].reverse()
        newarr[i] += tmp
    return newarr

def arr_printer(arr, N, d):
        




for T in range(int(input())):
    N, d = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(f"#{T+1}")
    arr_printer(arr, N, d)