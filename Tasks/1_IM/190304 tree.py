
##########################################################################
##########################################################################
# Binary Tree : Pre-order Traversal
# using 2D List and DFS


input1 = '13'
input2 = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# 전위 순회.. Pre-order

V = int(input1)
nodes = list(map(int, input2.split()))

tree = [[] for _ in range(V+1)]
for i in range(0, len(nodes), 2):
    a, b = nodes[i:i+2]
    tree[a] += [b]

vis = [1] + [0] * V
route = []

curr = 1  # start at 1
route.append(curr)
vis[curr] = 1
stack = [curr]

while 0 in vis:
    if not tree[curr]:  # curr is not a parent node
        while 1:
            curr = stack.pop()
            if [x for x in tree[curr] if not vis[x]]:  # until there is a child node to visit
                break
    else:  # curr is a parent node
        curr = [x for x in tree[curr] if not vis[x]][0]
        route.append(curr)
        vis[curr] = 1
        stack.append(curr)

print(*route)


##############################################################################################
##############################################################################################

# Pre-order Traversal using Doubly Linked List format
# - "prev" = left child
# - "next" = right child

input1 = '13'
input2 = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'


def preorder(T):  # T: starting point
    if T:
        print("%d" % T, end=" ")
        preorder(tree[T][0])
        preorder(tree[T][1])


n = int(input1)
tree = [[0] * 2 for _ in range(n+1)]
templ = list(map(int, input2.split()))

for i in range(len(templ) // 2):
    par, ch = templ[i*2], templ[i*2+1]
    if not tree[par][0]:
        tree[par][0] = ch
    else:
        tree[par][1] = ch

print(tree)
preorder(1)

