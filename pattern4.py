n = int(input())
spaces = 0

for i in range(n):
    for j in range(spaces):
        print(" ",end = "")
    
    for star in range(n):
        print("*",end = "")
    spaces = spaces + 1
    print()
