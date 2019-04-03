import sys
sys.stdin = open('Input/2117.txt', 'r')

""" 2117. [모의 SW 역량테스트] 홈 방범 서비스

Maximum number of houses covered; no loss

"""

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    Max = 0




    print(f"#{T} {Max}")

