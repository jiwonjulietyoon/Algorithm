# 주사위 쌓기

"""
0 A - 5 F
1 B - 3 D
2 C - 4 E
3 D - 1 B
4 E - 2 C
5 F - 0 A

"""

def opposite(idx):
    return [5, 3, 4, 1, 2, 0][idx]

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

Max = 0  # max sum encountered

for x in range(1, 7):  # try all 6 sides of the first die, starting with 1
    Sum = 0
    bottom = x
    for i in range(N):  # build Sum starting from first die
        idx = dice[i].index(bottom)
        top = dice[i][opposite(idx)]
        sides = list(range(1, 7))
        sides.remove(bottom)
        sides.remove(top)
        Sum += max(sides)
        bottom = top  # for the next die
    if Sum > Max:
        Max = Sum

print(Max)

