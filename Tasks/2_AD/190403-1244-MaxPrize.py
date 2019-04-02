# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

import sys
sys.stdin = open('../Input/1244.txt', 'r')

for T in range(1, int(input())+1):
    inp = input().split()
    num, cnt = [int(x) for x in inp[0]], int(inp[1])
    print(num, cnt)




    # print(f"#{T} {Max}")