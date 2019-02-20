"""
1부터 주어진 횟수까지 2를 곱한 값들을 출력하기

8 -> 1 2 4 8 16 32 64 128 256

"""

num = int(input())
for i in range(num + 1):
    print(2 ** i, end=' ')

