# 1979. 어디에 단어가 들어갈 수 있을까


for T in range(int(input())):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    ans = 0
    for y in range(N):      # check by row
        cnt = 0  # number of consecutive white cells
        for x in range(N):  # move through cells horizontally
            if arr[y][x]:    # white cell
                cnt += 1
                if x == N-1 and cnt == K:  # if cell is at the rightmost column and there have been 3 consecutive white cells
                    ans += 1
            else:           # black cell
                if cnt == K:
                    ans += 1
                cnt = 0
    for x in range(N):    # check by column
        cnt = 0
        for y in range(N):  # move through cells vertically
            if arr[y][x]:   # white cell
                cnt += 1
                if y == N-1 and cnt == K:
                    ans += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f"#{T+1} {ans}")