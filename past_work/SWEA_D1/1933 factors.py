"""
1 ~ 1000 사이의 정수 N이 주어질 때 N의 약수를 오름차순으로 출력하기

예: 10 -> 1 2 5 10
"""

N = int(input())
factors = [i for i in range(1, N + 1) if N % i == 0]
print(' '.join(map(str, factors)))

