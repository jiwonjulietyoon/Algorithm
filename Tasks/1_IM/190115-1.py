# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max


T = int(input())
for i in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    print(f"#{i+1} {max(num) - min(num)}")








# without using min() max() built-in functions
for T in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    Max = num[0]
    Min = num[0]
    for i in range(1, N):
        if num[i] > Max:
            Max = num[i]
        if num[i] < Min:
            Min = num[i]
    print(f"#{T+1} {Max - Min}")

