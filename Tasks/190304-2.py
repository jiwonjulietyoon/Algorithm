# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def completeBinaryTree(T, i, N):
    global points
    if i < N:
        T = Node(points[i])
        T.left = completeBinaryTree(T.left, 2*i+1, N)
        T.right = completeBinaryTree(T.right, 2*i+2, N)
    return T


# def inOrder(T):
#     global num, val, cnt
#     if T:
#         inOrder(T.left)
#         cnt += 1
#         num.append(T.data)
#         val.append(cnt)
#         inOrder(T.right)

def inOrder(T):
    if T:
        inOrder(T.left)
        print(T.data, end=" ")
        inOrder(T.right)


for TC in range(int(input())):
    N = int(input())
    points = list(range(1, N + 1))

    T = completeBinaryTree(None, 0, N)
    # num = []
    print(T)

    # print(TC+1)
    # inOrder(T)


    # print("#{} {} {}".format(T+1, root, ans)) # ans: N//2 번 노드
    # print(TC+1)
    # print(num)
    # print(val)


