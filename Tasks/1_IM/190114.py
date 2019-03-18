# 1206
# 
# 
# 건물 조망권 (좌우로 최소 2칸이 확보될 때 조망권이 있다고 한다.)



for i in range(10):
    N = int(input())
    b = list(map(int, input().split()))
    Sum = 0
    for x in range(2, N - 2):
        if b[x] > max(b[x-2:x]) and b[x] > max(b[x+1:x+3]):
            Sum += min(b[x]-b[x-1], b[x]-b[x-2], b[x]-b[x+1], b[x]-b[x+2])
    print(f"#{i+1} {Sum}")

