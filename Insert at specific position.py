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

def addNodeAtTail(head,element):
    newBlock = Node(element)
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

def insertAtSpecificPosition(head,position,val):
    newBlock = Node(val)
    index = 1
    curr = head
    while index != position - 1:
        index += 1
        curr = curr.next
    nextNode = curr.next
    newBlock.next = nextNode
    nextNode.prev = newBlock
    curr.next = newBlock
    newBlock.prev = curr
    return head

n = int(input())
l = map(int,input().split())
position,val  = list(map(int,input().split()))
head = None 
for ele in l:
    head = addNodeAtTail(head, ele)
 
printLefttoRight(head)
printRighttoLeft(head)   
 
head = insertAtSpecificPosition(head,position,val)
 
printLefttoRight(head)
printRighttoLeft(head)     
