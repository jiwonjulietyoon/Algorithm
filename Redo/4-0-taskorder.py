import sys
sys.stdin = open('Input/input1267.txt', 'r')

"""
4. Stack 1

1267. [S/W 문제해결 응용] 10일차 - 작업순서



"""



for T in range(1, 11):
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    prereq = [[] for _ in range(V+1)]
    for i in range(0, 2*E, 2):
        a, b = tmp[i:i+2]
        prereq[b] += [a]
    done = [1] + [0] * V
    route = []

    i = 1
    while 0 in done:
        if not done[i] and 0 not in [done[x] for x in prereq[i]]:
            route.append(i)
            done[i] = 1
        i += 1
        if i == V+1:
            i = 1

    print(f"#{T}", end=" ")
    print(*route, sep=" ")