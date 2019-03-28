
import sys
sys.stdin = open('../Input/5209.txt', 'r')


def backtrack(k, Sum):
    global arr, N, Min, vis
    if Sum > Min:
        return
    if k == N:
        if Sum < Min:
            Min = Sum
    else:
        for i in range(N):
            if not vis[i]:
                vis[i] = 1
                backtrack(k+1, Sum+arr[k][i])
                vis[i] = 0


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min = sum([arr[i][i] for i in range(N)])
    vis = [0]*N
    backtrack(0, 0)

    print(f"#{T+1} {Min}")