# 딱지 놀이

"""
star4, circle3, square2, triangle1

"""


import sys
sys.stdin = open('../Input/14696.txt', 'r')
# sys.stdin = open('../Input/14696-2.txt', 'r')


N = int(input())  # number of rounds
cards = [list(map(int, input().split())) for _ in range(2*N)]

print(*cards, sep="\n")
print()

res = []  # result of each round

for i in range(0, 2*N, 2):
    # A's card: cards[i]  // B's card: cards[i+1]
    shapes = [[0, 0] for _ in range(4)]
    for p in range(2):
        n = cards[i+p][0]
        for j in range(1, n+1):
            shapes[cards[i+p][j]-1][p] += 1
    print(*shapes, sep="\n")
    print()





