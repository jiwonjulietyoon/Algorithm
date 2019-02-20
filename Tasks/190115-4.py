# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    Max = 0
    Min = sum(num)
    for x in range(N-M+1):
        if sum(num[x:x+M]) > Max:
            Max = sum(num[x:x+M])
        if sum(num[x:x+M]) < Min:
            Min = sum(num[x:x+M])
    print(f"#{t+1} {Max - Min}")





## do not recompute
"""
[0][1][2][3][4][5][6][7][8][9] 여기서 숫자 3개씩의 구간합을 구한다고 할 때:

매번 sum([0][1][2]), sum([1][2][3]), sum([2][3][4]) 이렇게 새로 구하는 것보다

sum([0][1][2]), sum([0][1][2])-[0]+[3], (sum([0][1][2])-[0]+[3])-[1]+[4] 이런 식으로
이미 연산해놓았던 값들을 최대한 재활용하는 편이 장기적으로 보았을 때 훨씬 효율적이다

특히 주어진 숫자 리스트의 길이가 기하급수적으로 길어지는 경우, 
그리고 아주 큰 개수의 구간합을 구해야 할 경우, 매번 새로이 sum()을 쓰면 연산 횟수가 많아진다.



"""

