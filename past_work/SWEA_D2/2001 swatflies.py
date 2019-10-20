# 2001. 파리 퇴치


for T in range(int(input())):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    sumlist = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                s += sum(arr[i+k][j:j+M])
            sumlist.append(s)
    print(f"#{T+1} {max(sumlist)}")






for T in range(int(input())):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                s += sum(arr[i+k][j:j+M])
            if Max < s:
                Max = s
    print(f"#{T+1} {Max}")



for T in range(int(input())):
    N = list(map(int, input().split()))
    arr = []
    for _ in range(N[0]):
        arr.append(list(map(int, input().split())))
    Max = 0
    for i in range(N[0]-N[1]+1):
        for j in range(N[0]-N[1]+1):
            s = 0
            for k in range(N[1]):
                s += sum(arr[i+k][j:j+N[1]])
            if Max < s:
                Max = s
    print(f"#{T+1} {Max}")