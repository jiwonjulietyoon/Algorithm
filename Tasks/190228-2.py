# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, idx, data):
        if self.head == None:  # empty list, insert as first item
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            return
        if idx == 0:  # list has at least one item & insert as first item
            newNode = Node(data, None, self.head)
            self.head.prev = newNode
            self.head = newNode
            return
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx and curr.getNext() == None:  # insert as last item of list
                newNode = Node(data, curr)
                curr.next = newNode
                self.tail = newNode
                return
            if cnt + 1 == idx:  # insert after curr
                newNode = Node(data, curr, curr.next)
                curr.next.prev = newNode
                curr.next = newNode
                return
            cnt += 1
            curr = curr.getNext()

    def insertList(self, l, N): # l: list to insert
        curr = self.head
        cnt = 0
        l.reverse()
        while curr:
            if curr.data > l[-1]:
                for i in range(N):
                    self.insert(cnt, l[i])
                return
            curr = curr.getNext()
            cnt += 1
        for i in range(N):
            self.insert(cnt, l[i])
        return

    def popLast(self):
        curr = self.tail
        last = curr.data
        curr.prev.next = None
        self.tail = curr.prev
        return last



for T in range(int(input())):
    N, M = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(M)]

    myList = DoublyLinkedList()

    for x in num:
        myList.insertList(x, N)

    print(f"#{T+1}", end=" ")
    for i in range(10):
        print(myList.popLast(), end=" ")
    print()






#########################################################
# 시간 제한 초과 

# def insert_list(main, sub, N): # insert sub into main; N = len(sub)
#     for i in range(len(main)):
#         if main[i] > sub[0]:
#             subrev = list(reversed(sub))
#             for j in range(N):
#                 main.insert(i, subrev[j])
#             return main
#     return main.extend(sub)


# for T in range(int(input())):
#     N, M = map(int, input().split())
#     num = [list(int, input().split()) for _ in range(M)]
#         # reverse later in order to insert in the same index number every time
    
#     ans = []
#     ans.append(num.pop(0))

#     while num:
#         sub = num.pop(0)
#         main = insert_list(main, sub, N)[:]

#     main.reverse()
#     main = main[:10]

#     print(f"#{T+1}", end=" ")
#     print(*main, sep=" ")

