

import sys
# sys.stdin = open('../Input/2606.txt', 'r')
sys.stdin = open('../Input/tmp.txt', 'r')


def DFS():
    global nodes, vis, stack, c
    while stack:
        print(c)
        tmp = [a for a in nodes[c] if not vis[a]]
        if tmp:
            c = tmp[0]
            stack.append(c)
            vis[c] = 1
        else:
            c = stack.pop()

N = int(input())
E = int(input())
temp = [list(map(int, input().split())) for _ in range(E)]

vis = [0] * (N+1)

nodes = [[] for _ in range(N+1)]
for x in temp:
    nodes[x[0]] += [x[1]]
    nodes[x[1]] += [x[0]]

c = 1
stack = [None, c]
vis[c] = 1
DFS()

print(vis)
print(sum(vis) - 1)


