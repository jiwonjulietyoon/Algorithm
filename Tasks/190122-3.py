# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

def binary(l, r, idx):   # idx = idx to search for
    cnt = 0
    while(1):
        c = int((l+r)/2)
        cnt += 1
        if c == idx:
            break
        if idx >= l and idx < c:
            r = c
        elif idx > c and idx <= r:
            l = c
    return cnt

for T in range(int(input())):    # test case
    P, Pa, Pb = map(int, input().split())
    if binary(1, P, Pa) < binary(1, P, Pb):
        win = "A"
    elif binary(1, P, Pa) > binary(1, P, Pb):
        win = "B"
    else:
        win = 0
    print(f"#{T+1} {win}")