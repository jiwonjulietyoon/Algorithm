
















####################################################################

def BFS(v):
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v)
            for w in edges[v]:
                if not visited[w]:
                    q.append(w)


N = 7  # number of vertices (nodes)
input1 = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'  # all edges
tmp = list(map(int, input1.split()))
edges = [[] for _ in range(N+1)]
for i in range(0, len(tmp), 2):
    a, b = tmp[i], tmp[i+1]
    edges[a] += [b]
    edges[b] += [a]
visited = [1] + [0]*N

BFS(1)


################################################################################


def DFS(c):
    global vis, stack, edges
    # if not vis[c]:
    vis[c] = 1
    print(c)
    # stack.append(c)
    for x in edges[c]:
        if not vis[x]:
            DFS(x)
    # else:
    #     c = stack.pop()

N = 7  # number of vertices (nodes)
input1 = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'  # all edges

tmp = list(map(int, input1.split()))
edges = [[] for _ in range(N+1)]
for i in range(0, len(tmp), 2):
    a, b = tmp[i], tmp[i+1]
    edges[a] += [b]
    edges[b] += [a]
print(edges)

vis = [1] + [0]*N
# stack = []

c = 1  # current node
DFS(c)


