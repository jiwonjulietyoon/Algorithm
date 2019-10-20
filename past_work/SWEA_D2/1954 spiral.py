# 1954. 달팽이 숫자


for T in range(int(input())):
    N = int(input())
    arr = [[0] * N for i in range(N)]
    num, row, col, R, C = 1, 0, 0, N, N

    while(1):
        for i in range(col, C):
            arr[row][i] = num
            num += 1
        row += 1
        if row == R or col == C:
            break

        for i in range(row, R):
            arr[i][C-1] = num
            num += 1
        C -= 1
        if row == R or col == C:
            break

        for i in range(C-1, col-1, -1):
            arr[R-1][i] = num
            num += 1
        R -= 1
        if row == R or col == C:
            break

        for i in range(R-1, row-1, -1):
            arr[i][col] = num
            num += 1
        col += 1
        if row == R or col == C:
            break

    print(f"#{T+1}")
    for i in range(N):
        print(" ".join(map(str, arr[i])))