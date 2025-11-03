class student :
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudents(self):
        print("Roll Number:",self.rollno)
        print("Name:",self.name) 
        print("Course:",self.course) 
#inheritence
class test(student):
    def getmarks(self,Marks):
        self.Marks=Marks
    def displayMarks(self):
        print("Total Marks :",self.Marks)
r=int(input("Enter The Roll Number :"))
n=input("Enter The Name :")  
c=input("Enter The Course :")
m=int(input("Enter The Marks :")) 
print("Result") 
stud1=test()
stud1.getdata(r,n,c)
stud1.getmarks(m)
stud1.displaystudents()
stud1.displayMarks()
       
