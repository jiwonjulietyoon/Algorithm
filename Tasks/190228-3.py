# 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next

class DoublyLinkedList: # Doubly Linked List w/ head & tail
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def insert(self, idx, data):
        if self.head == None:  # insert as first item into an empty list
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        if idx == 0: # insert as first item
            newNode = Node(data, None, self.head)
            self.head.prev = newNode
            self.head = newNode
            self.size += 1
            return

    def insertBtw(self, idx): # insert item in given idx position; value = sum of two adjacent items
        if idx == 0: # add as last item; value = head.data + tail.data
            data = self.head.data + self.tail.data
            newNode = Node(data, self.tail)
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
            return
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                data = curr.data + curr.next.data
                newNode = Node(data, curr, curr.next)
                curr.next.prev = newNode
                curr.next = newNode
                self.size += 1
                return
            cnt += 1
            curr = curr.getNext()

    def getAllNodesRev(self): # list of all nodes, in reversed order
        nodes = []
        curr = self.tail
        while curr:
            nodes.append(curr.data)
            curr = curr.getPrev()
        return nodes


for T in range(int(input())):
    N, M, K = map(int, input().split()) # M spaces backward; repeat K times
    num = list(map(int, input().split()))[::-1]

    myList = DoublyLinkedList()
    for x in num:
        myList.insert(0, x)

    idx = 0
    for _ in range(K):
        idx += M
        idx %= myList.size
        myList.insertBtw(idx)
        idx = myList.size-1 if idx == 0 else idx

    ans = myList.getAllNodesRev()[:10]

    print(f"#{T+1}", end=" ")
    print(*ans, sep=" ")