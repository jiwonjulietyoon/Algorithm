# 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기

# import sys
# sys.stdin = open('input1258.txt', 'r')

###################################################









##################################################
# 2nd try

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0]*N for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] and not vis[i][j]:
                r, c = i, j
                y = x = 1
                vis[r][c] = 1
                while arr[r][c+1]:
                    vis[r][c + 1] = 1
                    x += 1
                    c += 1
                while arr[r+1][c]:
                    vis[r + 1][j:j + x] = [1] * x
                    y += 1
                    r += 1
                ans.append([y, x])

    ans.sort(key=lambda x: (x[0]*x[1], x[0]))

    print(f"#{T+1} {len(ans)}", end=" ")
    for a in ans:   
        print(*a, end=" ")
    print()



###############################################################

# 1st try

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0]*N for _ in range(N)]
    ans = []
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not vis[i][j]:
                r, c = i, j
                y = x = 1
                while arr[r][c+1]:
                    x += 1
                    c += 1
                while arr[r+1][c]:
                    y += 1
                    r += 1
                ans.append([y, x])
                for R in range(i, i+y):
                    for C in range(j, j+x):
                        vis[R][C] = 1
 
    ans.sort(key=lambda x: (x[0]*x[1], x[0]))
 
    print(f"#{T+1} {len(ans)}", end=" ")
    for a in ans:
        print(*a, sep=" ", end=" ")
    print()