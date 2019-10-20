"""
주어진 숫자부터 0까지 순서대로 출력하기
"""


num = int(input())
for i in range(num, -1, -1):
    print(i, end=' ')