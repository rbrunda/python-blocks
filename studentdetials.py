class Box:
    def __init__(self,currname,currrollno,currdbmsmarks,
    currpythonmarks,currcmarks,currosmarks,currcnmarks):
        self.name=currname
        self.rollno=currrollno
        self.dbmsmarks=currdbmsmarks
        self.pythonmarks=currpythonmarks
        self.cmarks=currcmarks
        self.osmarks=currosmarks
        self.cnmarks=currcnmarks

student1 = Box("Harika","5A1",78,67,77,89,46)
print(student1.name,student1.rollno,student1.dbmsmarks,student1.pythonmarks,student1.cmarks,student1.osmarks,
      student1.cnmarks)

student2 = Box("Swapna","5A2",38,65,97,59,41)
print(student2.name,student2.rollno,student2.dbmsmarks,student2.pythonmarks,student2.cmarks,student2.osmarks,
      student2.cnmarks)



student3 = Box("Sushma","5A3",88,95,47,89,31)
print(student3.name,student3.rollno,student3.dbmsmarks,student3.pythonmarks,student3.cmarks,student3.osmarks,
      student3.cnmarks)
