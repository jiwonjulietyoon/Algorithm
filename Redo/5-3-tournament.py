import sys
sys.stdin = open('Input/input4880.txt', 'r')

"""
5. Stack 2

4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임


"""

def winner(a, b):
    if a[1] == 1 and b[1] == 3:
        return a
    if a[1] == 3 and b[1] == 1:
        return b
    return a if a[1] >= b[1] else b

def divide(cards):
    global new
    l = len(cards)
    if l == 1:
        new.append(cards[0])
    elif l == 2:
        new.append(winner(cards[0], cards[1]))
    else:
        m = l//2 + 1 if l % 2 else l//2
        left = cards[:m]
        right = cards[m:]
        divide(left)
        divide(right)


for T in range(int(input())):
    N = int(input())
    cards = list(enumerate(map(int, input().split()), start=1))
    new = []

    while len(cards) > 1:
        divide(cards)
        cards = new[:]
        new = []

    print(f"#{T+1} {cards[0][0]}")