## 1209. [S/W 문제해결 기본] 2일차 - Sum


for T in range(10):
    arr = []
    t = int(input())
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    Max = 0
    for i in range(100):
        if sum(arr[i]) > Max:
            Max = sum(arr[i])
    arr2 = list(zip(*arr))
    for i in range(100):
        if sum(arr2[i]) > Max:
            Max = sum(list(zip(*arr))[i])
    diag1 = diag2 = 0
    for i in range(100):
        diag1 += arr[i][i]
        diag2 += arr[99-i][i]
    print(f"#{T+1} {max(Max, diag1, diag2)}")


