# 직사각형

import sys
sys.stdin = open('../Input/2527.txt', 'r')

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    ans = 'a'

    # (a) 직사각형
    if x2 > p1 or x1 > p2 or y1 > q2 or y2 > q1:
        ans = 'd'

    # (b) 선분  // (c) 점
    elif y1 == q2 or y2 == q1:
        ans = 'b'
        if x2 == p1 or x1 == p2:
            ans = 'c'
    elif x1 == p2 or x2 == p1:
        ans = 'b'
        if y1 == q2 or y2 == q1:
            ans = 'c'

    print(ans)
