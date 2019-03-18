# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로




def findRoute(V, E, nodes, start, end):
    visited = [0] * V
    stack = [0] * V
    top = -1
    c = start
    nodes_par = [nodes[i][0] for i in range(E)]
    nodes_ch = [nodes[i][1] for i in range(E)]

    while(1):
        if c in nodes_par and 0 in [visited[nodes[i][1]-1] for i in range(E) if nodes[i][0] == c]:
            visited[c-1] = True
            top += 1
            stack[top] = c
            for i in range(E):
                if nodes[i][0] == c and not visited[nodes[i][1]-1]:
                    c = nodes[i][1]
                    if c == end:
                        return 1
                    visited[c-1] = True
                    break
        else:
            if c not in nodes_ch and 0 not in [visited[nodes[i][1] - 1] for i in range(E) if nodes[i][0] == c]:
                return 0
            c = stack[top]
            top -= 1

for T in range(int(input())):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    print(f"#{T+1} {findRoute(V, E, nodes, start, end)}")






# e.g TEST CASE 1
# 1   # tc number
# 6 5 # V, E
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6
# 1 6 # S, G