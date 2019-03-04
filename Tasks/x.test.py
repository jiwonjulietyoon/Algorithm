input1 = '13'
input2 = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# 전위 순회..

def preorder(T):
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

preorder(1)

