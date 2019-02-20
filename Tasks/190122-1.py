# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

for T in range(int(input())):     # test case
    N = int(input())       # number of areas to color
    color1 = []
    color2 = []
    for _ in range(N):
        r1, c1, r2, c2, col = map(int, input().split())
        if col == 1:      # color is red
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    color1.append((i, j))
        else:             # color is blue
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    color2.append((i, j))
    common = set(color1).intersection(set(color2))
    print(f"#{T+1} {len(common)}")