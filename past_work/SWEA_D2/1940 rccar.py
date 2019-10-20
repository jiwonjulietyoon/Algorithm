# 1940. 가랏! RC카!

for T in range(int(input())):
    N = int(input())
    dis = vel = 0
    for _ in range(N):
        comm = list(map(int, input().split()))
        if comm[0] == 1: # accelerate
            vel += comm[1]
        elif comm[0] == 2: # decelerate
            if comm[1] > vel:
                vel = 0
            else:
                vel -= comm[1]
        dis += vel
    print(f"#{T+1} {dis}")