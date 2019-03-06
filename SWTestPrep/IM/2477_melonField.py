# 참외밭

import sys
sys.stdin = open('../Input/2477.txt', 'r')

N = int(input())
field = [list(map(int, input().split())) for _ in range(6)]

NS = 0
EW = 0

for line in field:
    if line[0] in [3, 4]:  # N, S
        if line[1] > NS:
            NS = line[1]
    else:  # E, W
        if line[1] > EW:
            EW = line[1]
main = NS * EW

for i in range(6):
    if field[i][0] == field[(i+2) % 6][0] and field[(i+1) % 6][0] == field[(i+3) % 6][0]:
        break
sub = field[(i+1) % 6][1]*field[(i+2) % 6][1]

area = main - sub
print(area * N)


