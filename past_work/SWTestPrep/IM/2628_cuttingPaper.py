"""
종이자르기



"""

w, h = map(int, input().split())
N = int(input())  # number of cuts
cuts = [list(map(int, input().split())) for _ in range(N)]

hor = [0, h]  # apply to h
ver = [0, w]  # apply to w

for x in cuts:
    if x[0] == 0:  # cut horizontally
        hor.append(x[1])
    else:  # cut vertically
        ver.append(x[1])
hor.sort()
ver.sort()

Max = 0  # max area encountered

for i in range(1, len(hor)):
    for j in range(1, len(ver)):
        sub_h = hor[i] - hor[i-1]
        sub_w = ver[j] - ver[j-1]
        area = sub_w * sub_h
        if area > Max:
            Max = area

print(Max)




