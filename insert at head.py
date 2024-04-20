class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def printLefttoRight(head):
    
    curr = head
    while curr != None:
        print(curr.data,end = " ")
        curr = curr.next
    print()
def printRighttoLeft(head):
   
    tail = head
    while tail.next != None:
        tail = tail.next

    curr = tail
    while curr != None:
        print(curr.data,end =" ")
        curr = curr.prev
    print()

def addNodeAtHead(head,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    #left to right link
    newBlock.next = head
    #right to left link
    head.prev = newBlock
    return newBlock
def addNodeAtTail(head,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    tail = head
    while tail.next != None:
        tail = tail.next
    #left to right link
    tail.next = newBlock
    #right to left link
    newBlock.prev = tail
    return head


n = int(input())
l = map(int,input().split())
element = int(input())
head = None
for val in l:
    head = addNodeAtHead(head,val)
printRighttoLeft(head)
printLefttoRight(head)

head = addNodeAtTail(head,element)
printRighttoLeft(head)
printLefttoRight(head)
