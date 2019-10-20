# 1974. 스도쿠 검증


def isSudoku(arr):
    for i in range(9):   # row search
        if len(set(arr[i][:])) != 9:
            return False
    arr_t = list(zip(*arr))
    for i in range(9):   # row search transposed list
        if len(set(arr_t[i][:])) != 9:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for k in range(3):
                tmp.extend(arr[i+k][j:j+3])
            if len(set(tmp)) != 9:
                return False
    return True

for T in range(int(input())):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    if isSudoku(arr):
        ans = 1
    else:
        ans = 0
    print(f"#{T+1} {ans}")