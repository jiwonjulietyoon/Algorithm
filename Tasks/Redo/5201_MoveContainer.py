

import sys
sys.stdin = open('../Input/5201.txt', 'r')

for T in range(int(input())):
    N, M = map(int, input().split())
    # N containers, M trucks
    weight = list(map(int, input().split()))  # container weight
    truck = list(map(int, input().split()))  # truck capacity

    # move heaviest container first
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    Sum = 0
    i = 0
    for w in weight:
        if w > truck[i]:
            continue
        else:
            Sum += w
            i += 1
        if i == M:
            break

    # Sum = 0
    # for w in weight:
    #     if w > truck[0]:
    #         continue
    #     else:
    #         Sum += w
    #         truck.pop(0)
    #     if not truck:
    #         break

    print(f"#{T+1} {Sum}")

