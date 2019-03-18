###############################################################################
# 선형 큐 linear queue

Q = [0] * 10
front = rear = -1

def isEmpty():
    return True if front == rear else False

def isFull():
    return True if rear == len(Q)-1 else False

def enQueue(item):
    global rear
    if isFull():
        print("Full Queue")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        return "Empty Queue"
    else:
        front += 1
        return Q[front]

for i in range(1, 4):
    enQueue(i)

print(Q)

for _ in range(3):
    print(deQueue())


#######################################################################################

# 원형 큐 Circular Queue

cQ = [0] * 6
front = rear = 0   # 맨 앞자리의 front는 비워놓기

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Full Queue")
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        return "Empty Queue"
    else:
        front = (front+1) % len(cQ)
        return cQ[front]

print(cQ, front, rear)

for i in range(1, 6):
    enQueue(i)
print(cQ, front, rear)

enQueue(111)
print(cQ, front, rear)

for _ in range(6):
    print(deQueue())
print(cQ, front, rear)

enQueue(10)
print(cQ, front, rear)

##################################################################################

# Linked Queue

front = rear = None

class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def isEmpty():
    return front == None

def enQueue(item):
    global front, rear
    newNode = Node(item)           # create new node via Class "Node"
    if isEmpty():
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear
    if isEmpty():
        return "Empty Queue"
    item = front.item
    front = front.next
    if isEmpty():    # if front == None
        rear = None
    return item

def Qpeek():
    return front.item

def printQ():
    f = front
    s = ""
    while f:
        s += str(f.item) + " "
        f = f.next
    return s

for i in range(1, 6):
    enQueue(i)

print(front, rear, isEmpty())
print(printQ())

for _ in range(1, 4):
    print(deQueue())

print(front, rear, isEmpty())
print(printQ())

####################################################################

#우선순위 큐 Priority Queue (FIFO 가 아니라 우선순위 높은 순으로 나간다)



#####################################################################

# 마이쮸 문제


q = [0] * 100
f = r = -1
candis = 20
studcan = [1] * 20

sn = 1
nextsn = 2

r += 1
q[r] = sn
print("==>%d번 학생 : 입장하여 줄을 선다." % sn)
print("학생 줄 : ", q[f+1:r+1])

f += 1
sn = q[f]
print("%d번 학생 : 줄에서 나와..." % sn)
print("학생 줄 : ", q[f+1:r+1])

while candis > 0:
    if candis > studcan[sn]:
        candis -= studcan[sn]
    else:
        studcan[sn] = candis
        candis -= studcan[sn]
    print("%d번 학생 : 선생님한테 사탕 %d개를 받는다." % (sn, studcan[sn]))
    print("===== 남은 사탕의 개수는 %d개다." % candis)
    print()
    studcan[sn] += 1

    if candis <= 0:
        print("%d번 학생이 마지막 사탕을 받아간다." % sn)
        break

    r += 1
    q[r] = sn

    print("%d번 학생 : 다시 줄을 선다." % sn)
    print("학생 줄 : ", q[f+1:r+1])
    print("==> %d번 학생 : 입장하여 줄을 선다." % nextsn)

    r += 1
    q[r] = nextsn
    print("학생 줄 : ", q[f+1:r+1])

    nextsn += 1
    f += 1
    sn = q[f]
    print("%d번 학생 : 줄에서 나와 ..." % sn)
    print("학생 줄 : ", q[f+1:r+1])


##########################################################################

# BFS (Breadth First Search)

def BFS(G, v, n):   # G: graph  // v : start
    visited = [0] * n   # n : number of nodes
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(chr(t+65))
        for i in G[t]:
            if not visited[i]:
                queue.append(i)

# graph = {'A': ['B', 'C', 'D'], 'B': ['A', 'E', 'F'],
#          'C': ['A'], 'D': ['A', 'G', 'H', 'I'],
#          'E': ['B'], 'F': ['B'], 'G': ['D'],
#          'H': ['D'], 'I': ['D']}

graph = {0: [1, 2, 3], 1: [0, 4, 5],
         2: [0], 3: [0, 6, 7, 8],
         4: [1], 5: [1], 6: [3],
         7: [3], 8: [3]}

BFS(graph, 0, 9)

###################################################################################

# BFS 2

def BFS(G, v, n):   # G: graph  // v : start
    visited = [1] + [0] * n   # n : number of nodes
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)

graph = {1: [2, 3],
         2: [1, 4, 5],
         3: [1, 7],
         4: [2, 6],
         5: [2, 6],
         6: [4, 5, 7],
         7: [3, 6]}
# dictionary type: 나중에 속도가 느려질 수 있음

graph = [
    [0],
    [2, 3],
    [1, 4, 5],
    [1, 7],
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 6]
]

BFS(graph, 1, 7)




