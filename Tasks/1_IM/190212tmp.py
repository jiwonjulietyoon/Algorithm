

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