# 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, idx, data): # insert data before idx
        if idx == 0: # add data as first item
            newNode = Node(data, self.head)
            self.head = newNode
            return
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                newNode = Node(data, curr.next)
                curr.next = newNode
                return
            curr = curr.getNext()
            cnt += 1

    def delete(self, idx): # delete item in position idx
        if idx == 0: # delete first item
            self.head = self.head.next
            return
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                curr.next = curr.next.next
                return
            curr = curr.getNext()
            cnt += 1

    def change(self, idx, data): # change item in position idx to data
        curr = self.head
        cnt = 0
        while curr:
            if cnt == idx:
                curr.data = data
                return
            curr = curr.getNext()
            cnt += 1

    def getNode(self, idx): # get item in given idx position
        curr = self.head
        cnt = 0
        while curr:
            if cnt == idx:
                return curr.data
            curr = curr.getNext()
            cnt += 1
        return -1

for T in range(int(input())):
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))[::-1]
    add = [input().split() for _ in range(M)]

    myList = LinkedList()
    for x in num:
        myList.insert(0, x)

    for x in add:
        if x[0] == 'I':
            myList.insert(int(x[1]), x[2])
        elif x[0] == 'D':
            myList.delete(int(x[1]))
        elif x[0] == 'C':
            myList.change(int(x[1]), x[2])

    print(f"#{T + 1} {myList.getNode(L)}")