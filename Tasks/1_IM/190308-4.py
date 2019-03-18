# 1946. 간단한 압축 풀기

import sys
sys.stdin = open('../Input/input1946.txt', 'r')

for T in range(int(input())):
    N = int(input())
    code = [input().split() for _ in range(N)]

    doc = ""
    cnt = 0
    for x in code:
        for i in range(int(x[1])):
            doc += x[0]
            cnt += 1
            if not cnt % 10:
                doc += '\n'

    print("#{}".format(T+1))
    print(doc)
