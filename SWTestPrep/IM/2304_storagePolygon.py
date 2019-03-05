"""
창고 다각형

"""

N = int(input())
sticks = [list(map(int, input().split())) for _ in range(N)]

sticks.sort(key=lambda x: x[0])
print(sticks)

maxh = max(sticks, key=lambda x: x[1])  # tallest stick
maxidx = sticks.index(maxh)
# print(maxh, maxidx)

area = 0

# start ~ tallest stick
h = sticks[0][1]  # starting height
pos = sticks[0][0]  # x position
for i in range(1, maxidx+1):
    if sticks[i][1] > h: # upon meeting taller stick
        w = sticks[i][0] - pos
        # print(w, h)
        area += w*h
        pos = sticks[i][0]
        h = sticks[i][1]

# tallest stick
# tmp = maxh[0]
for tmp in range(N-1, maxidx-1, -1):
    if sticks[tmp][1] == maxh:
        break
area += (sticks[tmp][0]-maxidx+1)*maxh[1]
print((sticks[tmp][0]-maxidx+1)*maxh[1])
print(tmp)

# tallest stick ~ end
h = sticks[-1][1]
pos = sticks[-1][0]
for i in range(N-1, tmp-1, -1):
    if sticks[i][1] > h:  # upon meeting taller stick
        w = pos - sticks[i][0]
        print(w, h)
        area += w*h
        pos = sticks[i][0]
        h = sticks[i][1]

print(area)


