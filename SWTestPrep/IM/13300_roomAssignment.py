# 방 배정

import sys
sys.stdin = open('../Input/13300.txt', 'r')

N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
# 0: Female   / 1: Male

grades = [[0, 0] for _ in range(6)]
for x in students:
    if x[0]:  # Male
        grades[x[1]-1][1] += 1
    else:  # Female
        grades[x[1]-1][0] += 1

cnt = 0
for i in range(6):
    for j in range(2):
        if grades[i][j]: # if not 0
            q, r = divmod(grades[i][j], K)
            cnt += q
            if r:
                cnt += 1

print(cnt)



