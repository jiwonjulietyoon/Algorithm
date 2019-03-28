
import sys
sys.stdin = open('../Input/1865.txt', 'r')

def backtrack(k, prod):
    global arr, N, Max, vis
    if prod < Max:
        return
    if k == N:
        if prod > Max:
            Max = prod
    else:
        for i in range(N):
            if not vis[i]:
                vis[i] = 1
                backtrack(k+1, prod*arr[k][i]/100)
                vis[i] = 0


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    vis = [0]*N
    backtrack(0, 1)

    print("#%d %.6f" % (T+1, Max*100))