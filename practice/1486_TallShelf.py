# 1486. 장훈이의 높은 선반


import sys
sys.stdin = open('input/1486.txt')

def backtrack(k, Sum):
    global N, B, Min, a
    if Sum > Min:
        return
    if k == N:
        if B <= Sum < Min:
            Min = Sum
        return
    else:
        a[k] = 1
        backtrack(k+1, Sum+h[k])
        a[k] = 0
        backtrack(k+1, Sum)


for T in range(int(input())):
    N, B = map(int, input().split())  # N people, B = goal height
    h = list(map(int, input().split()))  # N heights

    Min = sum(h)

    a = [0] * N

    backtrack(0, 0)

    print(f"#{T+1} {Min-B}")