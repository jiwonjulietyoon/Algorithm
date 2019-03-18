# 1267. [S/W 문제해결 응용] 10일차 - 작업순서





for T in range(10):
    V, E = map(int, input().split())
    nodes = list(map(int, input().split()))

    prereq = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = nodes[2*i:2*i+2]
        prereq[b] += [a]

    route = []
    done = [True] + [0] * V

    i = 0
    while 0 in done:
        if not done[i] and 0 not in [done[x] for x in prereq[i]]:
            route.append(i)
            done[i] = True
        i += 1
        if i == V+1:
            i = 0

    print(f"#{T+1}", end=" ")
    print(*route, sep=" ")



















#####################################################################################

for T in range(10):
    V, E = map(int, input().split())
    nodes = list(map(int, input().split()))

    prereq = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = nodes[2*i:2*i+2]
        prereq[b] += [a]

    route = []
    done = [0] * (V+1)
    done[0] = True

    for i in range(1, V+1):
        if prereq[i] == []:
            route.append(i)
            done[i] = True
    
    i = 0
    while(1):
        if not done[i] and 0 not in [done[x] for x in prereq[i]]:
            route.append(i)
            done[i] = True
            i = 0
        else:
            i += 1
        if 0 not in done:
            break
    
    print(f"#{T+1}", end=" ")
    print(*route, end=" ")
    print()























for T in range(10):
    V, E = map(int, input().split())
    con = list(map(int, input().split()))

    route = []

    while(1):
        if len(route) == V:
            break
        par = [con[i] for i in range(0, len(con), 2)]
        ch = [con[i] for i in range(1, len(con), 2)]
        start = list(set(par)-set(ch))
        route.extend(start)

        idx = [i for i in range(0, len(con), 2) if con[i] in start]
        for x in idx[::-1]:
            if con[x+1] not in par:
                route.append(con[x+1])
            con[x:x+2] = []


        # par = [nodes[i][0] for i in range(len(nodes))]
        # ch = [nodes[i][1] for i in range(len(nodes))]
        # tmp = list(set(par) - set(ch))
        # for x in tmp:
        #     if x not in route:
        #         route.append(x)
        #     if x in par and
        # for i in nodes:
        #     if i[0] in route and i[1] in par:
        #         nodes.remove(i)
        #     elif i[0] in route and i[1] not in par:
        #         route.append(i[1])
        #         nodes.remove(i)

    print(f"#{T+1} {route}")











def DFS(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            DFS(w)
    stack.append(v)
 
for t in range(1, 11):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)] # adjacency list
    indeg = [0] * (V+1) # in-degree info
    visited, stack = [0] * (V+1), []
    edges = list(map(int, input().split()))
    for i in range(E):
        u, v = edges[i*2: i*2 + 2]
        G[u] += [v]
        indeg[v] += 1
    for i in range(1, V+1):
        if indeg[i] == 0:
            DFS(i)
    res = ''
    for v in stack[::-1]:
        res += f' {v}'
    print(f'#{t}{res}')











T = 10
 
for t in range(T):
    v, e = [int(x) for x in input().split()]
    edges = [int(x) for x in input().split()]
    graph = [[0]*v for _ in range(v)]
    count = [0]*(v)
    i=0
    while i<=len(edges)-1:
        graph[edges[i]-1][edges[i+1]-1]=1
        count[edges[i+1]-1]+=1
        i+=2
         
    queue = [-1]*v
    cur=-1
    start=0
    for i in range(v):
        if count[i]==0:
            queue[cur+1]=i
            cur+=1
    print("#{}".format(t+1),end="")
 
    for i in range(v):
        print(" {}".format(queue[i]+1), end="")
 
        for j in range(v):
            if graph[queue[i]][j]==1:
                graph[queue[i]][j]=0
                count[j]-=1
        for j in range(v):
            if count[j]==0 and j not in queue:
                queue[cur+1]=j
                cur+=1
    print()