"""
창고 다각형

"""

import sys
sys.stdin = open('../Input/tmp.txt', 'r')

N = int(input())
sticks = [list(map(int, input().split())) for _ in range(N)]
sticks.sort(key=lambda x: x[0])

maxstick = max(sticks, key=lambda x: x[1])  # first encountered tallest stick
maxidx = sticks.index(maxstick)  # idx of tallest stick, within "sticks"
Sum = 0  # area sum

############################ 1. Before Maximum

# search through sticks, from beginning until just before the first max stick
h = sticks[0][1]  # initial height
pos = sticks[0][0]  # initial x position
for i in range(1, maxidx):  # start from 2nd stick
    if sticks[i][1] > h:
        w = sticks[i][0] - pos
        Sum += w*h
        h, pos = sticks[i][1], sticks[i][0]
Sum += (maxstick[0]-pos)*h   # section right before the tallest interval

########################### 2. Maximum

# find maximum interval: maxidx ~ maxend
maxend = maxidx  # index of stick that marks the end of the tallest interval
for i in range(N-1, maxidx, -1):
    if sticks[i][1] == maxstick[1]:
        maxend = i
        break

# find area of tallest interval
Sum += maxstick[1]*(sticks[maxend][0]-sticks[maxidx][0]+1)

########################## 3. After Maximum

# search through sticks, from the end until just before the last max stick
h = sticks[-1][1]  # initial height
pos = sticks[-1][0]  # initial x position
for i in range(N-2, maxend, -1):
    if sticks[i][1] > h:
        w = pos - sticks[i][0]
        Sum += w*h
        h, pos = sticks[i][1], sticks[i][0]
Sum += (pos - sticks[maxend][0])*h

print(Sum)


