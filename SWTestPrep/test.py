N = int(input())
sticks = [list(map(int, input().split())) for _ in range(N)]

sticks.sort(key=lambda x: x[0])

maxh = max(sticks, key=lambda x: x[1])  # tallest stick
maxidx = sticks.index(maxh)

area = 0

# start ~ tallest stick
h = sticks[0][1]  # starting height
pos = sticks[0][0]  # x position
for i in range(1, maxidx+1):
    if sticks[i][1] > h: # upon meeting taller stick
        w = sticks[i][0] - pos
        area += w*h
        pos = sticks[i][0]
        h = sticks[i][1]

# tallest stick
for tmp in range(N-1, maxidx-1, -1):
    if sticks[tmp][1] == maxh:
        break
area += (sticks[tmp][0]-maxh[0]+1)*maxh[1]

# tallest stick ~ end
h = sticks[-1][1]
pos = sticks[-1][0]
for i in range(N-1, tmp-1, -1):
    if sticks[i][1] > h:  # upon meeting taller stick
        w = pos - sticks[i][0]
        area += w*h
        pos = sticks[i][0]
        h = sticks[i][1]

print(area)