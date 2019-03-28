
import sys
sys.stdin = open('../Input/5189.txt', 'r')


def backtrack(k, p, c, Sum):
    global arr, N, vis, Min
    if Sum > Min:
        return
    if k == N:
        Sum += arr[c][0]
        if Sum < Min:
            Min = Sum
    else:
        for i in range(1, N):
            if not vis[i]:
                vis[i] = 1
                pp, p, c = p, c, i
                s = Sum + arr[p][c]
                backtrack(k+1, p, c, s)
                vis[i] = 0
                p, c = pp, p


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    vis = [1] + [0]*(N-1)
    Min = 1000
    backtrack(1, 0, 0, 0)

    print(f"#{T+1} {Min}")


