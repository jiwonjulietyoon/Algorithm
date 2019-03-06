# 5356. 의석이의 세로로 말해요

import sys
sys.stdin = open('../Input/input5356.txt', 'r')

for T in range(int(input())):
    words = [input() for _ in range(5)]
    ans = ''
    maxl = len(max(words, key=lambda x: len(x)))
    for j in range(maxl):
        for i in range(5):
            try:
                ans += words[i][j]
            except:
                pass
    print("#{} {}".format(T+1, ans))