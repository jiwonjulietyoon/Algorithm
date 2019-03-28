
import sys
sys.stdin = open('../Input/1486.txt', 'r')


def power_set_r(a, k, Sum):
    global heights, N, B, Min
    if k == N:
        if B <= Sum < Min:
            Min = Sum
    elif Sum > Min:
        return
    else:
        a[k] = 1
        power_set_r(a, k+1, Sum+heights[k])
        a[k] = 0
        power_set_r(a, k+1, Sum)


for T in range(int(input())):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    Min = sum(heights)
    a = [0]*N
    power_set_r(a, 0, 0)

    print(f"#{T+1} {Min-B}")
