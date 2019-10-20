# 회장뽑기

import sys
sys.stdin = open('../Input/2660.txt', 'r')


def BFS(idx, N): # idx: idx of person to check
    global friends
    vis = [1] + [0]*N
    cnt = 0

    c = idx # current
    q = [c]
    vis[c] = 1

    while 0 in vis and q:
        tmp = q[:]
        for x in tmp:
            for y in friends[x]:
                if not vis[y]:
                    q.append(y)
                    vis[y] = 1
            q.remove(x)
        cnt += 1
    return cnt


N = int(input())
friends = [[] for _ in range(N+1)]

while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    friends[a] += [b]
    friends[b] += [a]

score = [100] + [0]*N
for i in range(1, N+1):
    score[i] = BFS(i, N)

Min = min(score)
ans = [x for x in range(1, N+1) if score[x] == Min]
print(Min, len(ans))
print(*ans, sep=" ")










