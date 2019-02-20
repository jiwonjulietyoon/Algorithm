"""
1부터 주어진 숫자만큼 모두 더한 합을 출력하기
"""

n = int(input())
Sum = 0
for i in range(n):
    Sum += i + 1
print(Sum)