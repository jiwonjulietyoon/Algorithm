# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리




# final answer

def find(graph, V, S, G):
    vis = [1] + [0] * V
    Q = [S]
    cnt = 0
    while (1):
        tmp = Q[:]
        for nd in tmp:
            vis[nd] = 1
            for x in graph[nd]:
                if not vis[x]:
                    Q.append(x)
            Q.remove(nd)
        if not Q:
            return 0
        cnt += 1
        if G in Q:
            break
    return cnt


for T in range(int(input())):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    graph = [ [] for _ in range(V+1)]
    for node in nodes:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    S, G = map(int, input().split())

    print(f"#{T+1} {find(graph, V, S, G)}")








# ########################################################################
# # seemed to work, but failed due to runtime error


# for T in range(int(input())):
#     V, E = map(int, input().split())
#     nodes = [list(map(int, input().split())) for _ in range(E)]
#     graph = [ [] for _ in range(V+1)]
#     for node in nodes:
#         graph[node[0]].append(node[1])
#         graph[node[1]].append(node[0])
#     S, G = map(int, input().split())
#     vis = [1] + [0] * V
#     Q = [S]
#     cnt = 0

#     while(1):
#         tmp = Q[:]
#         for nd in tmp:
#             vis[nd] = 1
#             for x in graph[nd]:
#                 if not vis[x]:
#                     Q.append(x)
#             Q.remove(nd)
#         cnt += 1
#         if G in Q:
#             break

#     print(f"#{T+1} {cnt}")








# ########################################################################
# # seemed to work, but failed due to runtime error

# def find(graph, V, S, G):
#     vis = [1] + [0] * V
#     stack = []
#     cnt = 0
#     c = S
#     while(1):
#         if c == G or 0 not in vis:
#             break
#         if 0 in [vis[x] for x in graph[c]]:
#             stack.append(c)
#             vis[c] = 1
#             for nd in graph[c]:
#                 if not vis[nd]:
#                     c = nd
#                     vis[c] = 1
#                     cnt += 1
#                     break
#         else:
#             cnt -= 1
#             c = stack.pop()
#     return cnt

# for T in range(int(input())):
#     V, E = map(int, input().split())
#     nodes = [list(map(int, input().split())) for _ in range(E)]
#     graph = [ [] for _ in range(V+1)]
#     for node in nodes:
#         graph[node[0]].append(node[1])
#         graph[node[1]].append(node[0])
#     S, G = map(int, input().split())
#     print(f"#{T+1} {find(graph, V, S, G)}")








# ########################################################
# # doesn't work, but BFS

# def BFS(graph, S, G):
#     vis = [1] + [0] * V
#     cnt = 0
#     Q = [S]
#     route = []

#     while Q:
#         t = Q.pop(0)
#         if not vis[t]:
#             vis[t] = 1
#             route.append(t)
#         for i in graph[t]:
#             if not vis[i]:
#                 Q.append(i)
#         cnt += 1
#         if G in route:
#             break
#     print(route)
#     return cnt


# for T in range(int(input())):
#     V, E = map(int, input().split())
#     nodes = [list(map(int, input().split())) for _ in range(E)]
#     graph = [ [] for _ in range(V+1)]
#     for node in nodes:
#         graph[node[0]].append(node[1])
#         graph[node[1]].append(node[0])
#     S, G = map(int, input().split())

#     print(f"#{T+1} {BFS(graph, S, G)}")
