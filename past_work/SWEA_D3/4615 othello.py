# 4615. 재미있는 오셀로 게임

import sys
sys.stdin = open('input4615.txt','r') 

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [ [0]*(N+1) for _ in range(N+1) ]
    mid = N//2
    arr[mid][mid], arr[mid+1][mid+1] = "W", "W"
    arr[mid+1][mid], arr[mid][mid+1] = "B", "B"

    disks = [list(map(int, input().split())) for _ in range(M)]
    for x in disks:
        

    print(f"#{T+1} {bl} {wh}")