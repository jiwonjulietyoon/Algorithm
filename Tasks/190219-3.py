# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임



def winner(sub):   # sub == pair of 2 cards OR just one card
    if len(sub) == 1:
        return sub[0]
    if (sub[0][1] == 1 and sub[1][1] == 3) or (sub[0][1] >= sub[1][1]):
        return sub[0]
    elif (sub[0][1] == 3 and sub[1][1] == 1) or (sub[0][1] < sub[1][1]):
        return sub[1]

def divide(group):
    if len(group) <= 2:
        return group
    else:
        if len(group) % 2:
            return divide(group[:len(cards)//2+1], group[len(cards)//2+1:])
        else:
            return divide(group[:len(cards)//2], group[len(cards)//2:])
# append
for T in range(int(input())):
    N = int(input())
    cards = list(enumerate(map(int, input().split()), start=1))

    while(1):
        

    print(f"#{T+1} {ans}")









###############################
### 5 out of 10 incorrect

def winner(left, right):
    if (left[1] == 1 and right[1] == 3) or (left[1] >= right[1]):
        return left
    elif (left[1] == 3 and right[1] == 1) or (left[1] < right[1]):
        return right


def tournament(cards):
    if len(cards) == 1:
        return cards[0]
    elif len(cards) == 2:
        return winner(cards[0], cards[1])
    else:
        if len(cards) % 2:
            return winner(tournament(cards[:len(cards)//2+1]), tournament(cards[len(cards)//2+1:]))
        else:
            return winner(tournament(cards[:len(cards)//2]), tournament(cards[len(cards)//2:]))


for T in range(int(input())):
    N = int(input())
    cards = list(enumerate(map(int, input().split()), start=1))

    print(f"#{T + 1} {tournament(cards)[0]}")