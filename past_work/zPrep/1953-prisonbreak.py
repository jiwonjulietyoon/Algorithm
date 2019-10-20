import sys
sys.stdin = open('Input/1953.txt', 'r')
# sys.stdin = open('Input/tmp.txt', 'r')

"""1953. [모의 SW 역량테스트] 탈주범 검거

"""
# direction: 0up, 1right, 2down, 3left
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# {moving direction: viable pipe shapes}
pipes_f = [
    (1, 2, 4, 7),  # up
    (1, 3, 4, 5),  # right
    (1, 2, 5, 6),  # down
    (1, 3, 6, 7)  # left
]
pipes_t = [
    (1, 2, 5, 6),  # up: down
    (1, 3, 6, 7),  # right: left
    (1, 2, 4, 7),  # down: up
    (1, 3, 4, 5)  # left: right
]

for T in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    vis = [[0]*M for _ in range(N)]  # Mark visited when appending to q
    cnt = 1
    q = [(R, C)]
    vis[R][C] = 1

    for _ in range(L-1):
        tmp, q = q, []
        for pos in tmp:
            for d in range(4):
                if arr[pos[0]][pos[1]] in pipes_f[d]:
                    y, x = pos[0]+dy[d], pos[1]+dx[d]
                    if 0 <= y < N and 0 <= x < M:
                        if not vis[y][x] and arr[y][x] in pipes_t[d]:
                            q.append((y, x))
                            cnt += 1
                            vis[y][x] = 1

    print(f"#{T} {cnt}")


