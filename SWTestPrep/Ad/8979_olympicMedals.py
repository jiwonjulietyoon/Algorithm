

import sys
sys.stdin = open('../Input/8979.txt', 'r')


N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if medals[i][0] == K:
        break

cnt = 1
while 1:
    if medals[i-cnt][1:] != medals[i][1:]:
        break
    cnt += 1

print(i-cnt+2)


"""
1      -3
2      
2
2      i = 4    4-3+1
5
5
7
8
9

"""


