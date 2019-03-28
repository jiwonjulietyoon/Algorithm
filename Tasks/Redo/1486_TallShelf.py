
import sys
sys.stdin = open('../Input/1486.txt', 'r')


def power_set_r():
    global heights, N, B, Min


for T in range(int(input())):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    Min = sum(heights)


    print(f"#{T+1} {Min-B}")
