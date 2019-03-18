# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

import sys
sys.stdin = open('../Input/1240.txt', 'r')

pattern = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
]

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    tmp = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == "1":
                tmp = 1
                break
        if tmp:
            break

    code = arr[i][j-55:j+1]
    dec = []
    for p in range(0, 56, 7):
        dec.append(pattern.index(code[p:p+7]))

    odd = sum(dec[0:7:2])*3
    even = sum(dec[1:7:2])

    if (odd+even+dec[-1]) % 10 == 0:
        print(f"#{T+1} {sum(dec)}")
    else:
        print(f"#{T+1} 0")





