class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def enQueue(head, val):
    print(val, "inserted")
    newNode = Node(val)
    if head == None:
        return newNode
  
    tail = head
    while tail.next != None:
        tail = tail.next
    tail.next = newNode
    return head


def deQueue(head):
    if head == None:
        print("Queue is empty")
        return None
  
    temp = head.next
    print(head.data)
    head.next = None
    return temp
  
def frontValue(head):
    if head == None:
        print("Queue is empty")
        return
    print(head.data)
    
def printQueue(head):
    if head == None:
        print("Queue is empty")
        return
  
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()

def printIsQueueEmpty(head):
    if head == None:
        print("Queue is empty")
    else:
        print("Queue is not empty")


head = None
n = int(input().strip())
while n > 0:
    word =list(map(int,input().split()))
    m = word[0]
    if m == 1:
        num = word[1]
        head = enQueue(head, num)
    elif m == 2:
        frontValue(head)
    elif m == 3:
        head = deQueue(head)
    elif m == 4:
        printQueue(head)
    else:
        printIsQueueEmpty(head)
    n -= 1
