Q = []
n = int(input().strip())
while n > 0:
    word = list(map(int, input().split()))
    m = word[0]
    if m == 1:
        num = word[1]
        Q.append(num)
        print(num, "inserted")
    elif m == 2:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print(Q[0])
    elif m == 3:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print(Q[0])
            Q.pop(0)
    elif m == 4:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            for ele in Q:
                print(ele, end = " ")
            print()
    else:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
      
    n -= 1

