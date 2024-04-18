class Box:
    def __init__(self,nameofStudent,rollno):
        self.name = nameofStudent
        self.rollno = rollno

obj1 = Box("bru",45)
obj2 = Box("anu",55)

print(obj1.name)
print(obj1.rollno)
print(obj2.name)
print(obj2.rollno)
