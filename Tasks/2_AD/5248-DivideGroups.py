
# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

import sys
sys.stdin = open('../Input/5248.txt', 'r')

# incorrect

TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))

    groups = []
    members = [1]*N

    for i in range(0, 2*M, 2):
        flag = 0
        for g in groups:
            if tmp[i] in g or tmp[i+1] in g:
                g.add(tmp[i])
                g.add(tmp[i+1])
                flag = 1
                break
        if not flag:
            groups.append({tmp[i], tmp[i+1]})
        members[tmp[i]-1] = 0
        members[tmp[i+1]-1] = 0

    print(f"#{T} {len(groups)+sum(members)}")
    print(groups)
    print(members)
