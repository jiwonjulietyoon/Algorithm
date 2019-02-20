# 6853 직사각형과 점 
# unable to submit as system does not accept Python codes


for T in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    dots = []
    for _ in range(N):
        dots.append(list(map(int, input().split())))
    In = On = Out = 0
    for dot in dots:
        if dot[0] > x1 and dot[0] < x2 and dot[1] > y1 and dot[1] < y2:
            In += 1
        elif (dot[0] >= x1 and dot[0] <= x2) and (dot[1] in (y1, y2)):
            On += 1
        elif (dot[1] >= y1 and dot[1] <= y2) and (dot[0] in (x1, x2)):
            On += 1
        else:
            Out += 1

    print(f"#{T+1} {In} {On} {Out}")