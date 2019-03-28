
import sys
sys.stdin = open('../Input/5202.txt', 'r')


for T in range(int(input())):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end = 0
    for x in time:
        if x[0] >= end:
            cnt += 1
            end = x[1]

    print(f"#{T+1} {cnt}")

