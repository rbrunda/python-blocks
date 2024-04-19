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
    newBlock.next = head
    head.prev = newBlock
    return newBlock


n = int(input())
l = map(int,input().split())
head = None
for ele in l:
    head = addNodeAtHead(head,ele)
printRighttoLeft(head)
printLefttoRight(head)
