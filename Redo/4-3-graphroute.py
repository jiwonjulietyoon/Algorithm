import sys
sys.stdin = open('Input/input4871.txt', 'r')

"""
4. Stack1

4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로



<< DFS >>

* return 1 when:
- curr == G

* Move down one level when:
- curr is a parent node => graph[node] is not empty
- at least 1 element in graph[curr] is unvisited => [a for a in graph[curr] if not vis[a]] is not empty

* Move up when:
- curr is not a parent node => graph[node] is empty
- => move up until [a for a in graph[curr] if not vis[a]] is not empty

* return 0 when:
- you need to move up one level but the stack is empty (nothing to pop)

"""

def DFS(curr, G):
    global graph, vis
    stack = [curr]
    vis[curr] = 1

    while 1:
        if curr == G:
            return 1
        if not graph[curr]: # curr is not a parent node
            while 1:
                if not stack: # stack is empty; can't move up
                    return 0
                curr = stack.pop()  # move up
                if [a for a in graph[curr] if not vis[a]]: # until there is a child node to visit
                    break
        else: # curr is a parent node
            tmp = [a for a in graph[curr] if not vis[a]]
            if not tmp: # return 0 when there all child nodes are visited
                return 0
            curr = tmp[0] # move down
            stack.append(curr)
            vis[curr] = 1


for T in range(int(input())):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    vis = [1] + [0] * V
    graph = [[] for _ in range(V+1)]
    for x in nodes:
        graph[x[0]] += [x[1]]

    print(f"#{T+1} {DFS(S, G)}")


