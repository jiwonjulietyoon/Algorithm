
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Function to insert nodes in level order
def insertLevelOrder(T, i, n):
    # Base case for recursion
    global arr
    if i < n:
        T = newNode(arr[i])

        # insert left child
        T.left = insertLevelOrder(T.left, 2*i+1, n)

        # insert right child
        T.right = insertLevelOrder(T.right, 2*i+2, n)
    return T


def inOrder(T):
    global num
    if T:
        inOrder(T.left)
        num.append(T.data)
        inOrder(T.right)


arr = list(range(1, 9))
n = len(arr)
T = insertLevelOrder(None, 0, n)

num = []
inOrder(T)

print(num)







##########################################################
# class newNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
#
# # Function to insert nodes in level order
# def insertLevelOrder(arr, T, i, n):
#     # Base case for recursion
#     if i < n:
#         T = newNode(arr[i])
#
#         # insert left child
#         T.left = insertLevelOrder(arr, T.left, 2*i+1, n)
#
#         # insert right child
#         T.right = insertLevelOrder(arr, T.right, 2*i+2, n)
#     return T
#
#
# def inOrder(T):
#     if T:
#         inOrder(T.left)
#         print(T.data, end=" ")
#         inOrder(T.right)
#
#
# arr = list(range(1, 9))
# n = len(arr)
# T = insertLevelOrder(arr, None, 0, n)
# inOrder(T)