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



#####################################
# Singly Linked List tmp

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
    def add(self, pre, data): # add (new) 'data' after 'pre'
        # need to convert 'pre' into an actual member object of the particular LinkedList object
        # at the moment, 'pre' is simply an 'int' or 'str' type (or whatever other data type inputted)
        #    (AttributeError: 'str' object has no attribute 'next')
        newNode = Node(data, pre.next)
        if pre == None:
            return 'Error'
        else:
            pre.next = newNode
            self.size += 1
            return f"{data} added after {pre.data}"
    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNext()


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
myList.printNode()
print("<<Inserting>>")
print(myList.add('A', 'AA'))
print("<<Size>>")
print(myList.getSize())

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









