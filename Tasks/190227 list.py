############################################



# 단순 연결 리스트 (Singly Linked List)

def addtoFirst(data):
    global Head
    Head = Node(data, Head)

def add(pre, data): # add 'data' following 'pre'
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)

def delete(pre): # delete node following 'pre'
    if pre == None or pre.link == None:
        print('Error')
    else:
        pre.link = pre.link.link



#################################################
################################################




# Singly Linked List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNext(self):
        return self.next

    def setNext(self, val):
        self.next = val


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addtoFirst(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return f"{newNode.data} prepended"

    def addtoLast(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = newNode
        self.size += 1
        return f"{newNode.data} appended"

    def add(self, pre, data): # add 'data' after 'pre'
        if self.head == None:
            return "Error: List is empty"
        curr = self.head
        while curr:
            if curr.data == pre:
                newNode = Node(data, curr.next)
                curr.next = newNode
                self.size += 1
                return f"{newNode.data} added after {curr.data}"
            curr = curr.getNext()
        return f"Error: Item '{pre}' not in list"

    def insert(self, idx, data): # insert 'data' into specified index position
        if type(idx) != int or idx < 0:
            return f"Error: Inserting position must be an integer (0 or above)"
        if idx == 0: # add as first item
            newNode = Node(data, self.head)
            self.head = newNode
            self.size += 1
            return f"{newNode.data} inserted into position {idx}"
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                newNode = Node(data, curr.next)
                curr.next = newNode
                self.size += 1
                return f"{newNode.data} inserted into position {idx}"
            curr = curr.getNext()
            cnt += 1
        return "Error: Position index out of range"

    def delete(self, idx): # delete item in given index position
        if type(idx) != int or idx < 0:
            return f"Error: Position must be an integer (0 or above)"
        if idx == 0: # delete first item
            self.head = self.head.next
            self.size -= 1
            return f"Item in position {idx} deleted"
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx:
                curr.next = curr.next.next
                self.size -= 1
                return f"Item in position {idx} deleted"
            curr = curr.getNext()
            cnt += 1
        return "Error: Position index out of range"

    def printNode(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.getNext()
        return nodes

    def getNode(self, idx): # get node of given index position
        curr = self.head
        cnt = 0
        while curr:
            if cnt == idx:
                return curr.data
            curr = curr.getNext()
            cnt += 1
        return "Error: Position index out of range"


# node1 = Node('A')
# print(node1.getData())
# node1.setData('AA')
# print(node1.getData())
# print(node1.getNext())
# node1.setNext('B')
# print(node1.getNext())


myList = LinkedList()
print("<<Inserting>>")
print(myList.addtoFirst(5))
print(myList.addtoFirst(15))
print(myList.addtoFirst(25))
print(myList.addtoLast('A'))
print(myList.addtoLast('B'))
print(myList.addtoLast('C'))
print("<<Printing>>")
print(*myList.printNode())
print("<<Inserting>>")
print(myList.add('A', 'AA'))
print(myList.add('BBB', 'BB'))
print(myList.insert(0, 'tmp'))

print("<<Printing>>")
print(*myList.printNode())
print("<<Size>>")
print(myList.getSize())

print("<<Inserting>>")
print(myList.insert(3, 'Z'))

print("<<Printing>>")
print(*myList.printNode())
print("<<Size>>")
print(myList.getSize())
print("===")
print(myList.getNode(5))

print("<<Deleting>>")
print(myList.delete(1))
print(myList.delete(0))
print(myList.delete(20))

print("<<Printing>>")
print(*myList.printNode())
print("<<Size>>")
print(myList.getSize())



###############################################################
################################################################


##### Doubly Linked List (working)

# data, next, prev, head, tail

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
        if self.head == None: # empty list, insert as first item
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            return f"{data} inserted as first item"
        if idx == 0: # list has at least one item & insert as first item
            newNode = Node(data, None, self.head)
            self.head.prev = newNode
            self.head = newNode
            return f"{data} inserted as first item"
        curr = self.head
        cnt = 0
        while curr:
            if cnt + 1 == idx and curr.getNext() == None: # insert as last item of list
                newNode = Node(data, curr)
                curr.next = newNode
                self.tail = newNode
                return f"{data} inserted as last item"
            if cnt + 1 == idx: # insert after curr
                newNode = Node(data, curr, curr.next)
                curr.next.prev = newNode
                curr.next = newNode
                return f"{data} inserted into position {idx}"
            cnt += 1
            curr = curr.getNext()
        return f"Error: Position index out of range"
    def getAllNodes(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.getNext()
        return nodes
    def popLast(self):
        curr = self.tail
        last = curr.data
        curr.prev.next = None
        self.tail = curr.prev
        return last


myList = DoublyLinkedList()
print(myList.insert(0, 'A'))
print(myList.insert(1, 'B'))




print(myList.insert(2, 'C'))
print(myList.getAllNodes())
print(myList.popLast())
print(myList.getAllNodes())
print(myList.head.data, myList.tail.data)



################################################################
##################################################################################



# MERGE SORT

def merge_sort(m):
    if len(m) <= 1:
        return m
    
    # 1. DIVIDE
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER : 분할된 리스트를 병합
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) and len(right): # 양쪽 리스트 둘 다에 원소가 남아있는 경우
        # 첫 원소끼리 비교하여 작은 것부터 result에 저장
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if len(left) > 0: # 왼쪽 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0: # 오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result

# e.g) print(merge_sort([69, 10, 30, 2, 16, 8, 31, 22]))

###############################################################################

# Priority Queue (Doubly Linked List) - unfinished

 # Priority Queue

sample = [1, 2, 5, 4, 3]

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def getData(self):
        return self.data
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next

class PriorityQueue:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    def getSize(self):
        return self.size
    def insert(self, data): # sort & insert
        if self.head == None: # if queue is empty
            newNode = Node(data)
            self.head = newNode
            self.size += 1
            return f"{newNode.data} added as first item"
        else: # there is at least one item in queue
            curr = self.head
            while 1:
                if curr.data > data:
                    newNode = Node(data)
                    curr.prev.next = newNode
                    newNode.next = curr
                    newNode.prev = curr.prev
                    curr.prev = newNode
                    self.size += 1
                    return f"{newNode.data} inserted after {newNode.prev.data}"
                if curr.getNext() == None:
                    break
                curr = curr.getNext()
            newNode = Node(data)
            curr.next = newNode
            newNode.pre = curr
            self.size += 1
            return f"{newNode.data} added as last item"
    def printNode(self):
        print("<<Printing Queue>>")
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNext()

samplePQ = PriorityQueue()

for x in sample:
    print(samplePQ.insert(x))

samplePQ.printNode()









