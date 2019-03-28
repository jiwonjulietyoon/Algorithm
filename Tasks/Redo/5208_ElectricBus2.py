
import sys
sys.stdin = open('../Input/5208.txt', 'r')


def backtrack(c, Sum):
    global station, N, Min
    if Sum > Min:
        return
    if station[c] >= N-1-c:
        if Sum < Min:
            Min = Sum
    else:
        for i in range(1, station[c]+1):
            backtrack(c+i, Sum+1)


for T in range(int(input())):
    station = list(map(int, input().split()))
    N = station[0]
    station = station[1:]

    Min = N
    backtrack(0, 0)
    print(f"#{T+1} {Min}")








