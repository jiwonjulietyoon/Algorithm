# 1486. 장훈이의 높은 선반

import sys
sys.stdin = open('../Input/1486.txt', 'r')


def power_set_r(k, Sum):
    global N, a, heights, Min
    if Sum > Min:
        return
    elif B <= Sum < Min:
        Min = Sum
        return
    elif k == N:
        return
    else:
        a[k] = 1
        power_set_r(k+1, Sum+heights[k])
        a[k] = 0
        power_set_r(k+1, Sum)


for T in range(int(input())):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort(reverse=True)

    Min = sum(heights)
    a = [0] * N
    power_set_r(0, 0)

    print(f"#{T+1} {Min-B}")







