# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addtoLast(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = newNode

    def insert(self, idx, data): # insert 'data' into specified index position
        if idx == 0: # add as first item
            newNode = Node(data, self.head)
            self.head = newNode
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                newNode = Node(data, curr.next)
                curr.next = newNode
                return
            curr = curr.getNext()
            cnt += 1

    def getNode(self, idx): # get node of given index position
        curr = self.head
        cnt = 0
        while curr:
            if cnt == idx:
                return curr.data
            curr = curr.getNext()
            cnt += 1


for T in range(int(input())):
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))
    add = [list(map(int, input().split())) for _ in range(M)]

    sample = LinkedList()
    for x in num:
        sample.addtoLast(x)
    for x in add:
        sample.insert(x[0], x[1])
    print(f"#{T+1} {sample.getNode(L)}")