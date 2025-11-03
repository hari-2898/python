class student :
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudents(self):
        print("Roll Number:",self.rollno)
        print("Name:",self.name) 
        print("Course:",self.course) 
    def displaystudent (self):
        print("Roll Number:", self.rollno)
        print("Course:", self.course)
        print("Name:", self.name)
#Inheritance
class Test (student):
    def getMarks (self, marks):
     self.marks=marks
    def displayMarks(self):
        print ("Total Marks:", self.marks)
#Multilevel Inheritance
class Result (Test):
    def calculateGrade (self):
     if self.marks>480: self.grade ="Distinction"
     elif self.marks>360: self.grade="First Class"
     elif self.marks>240: self.grade="Second Class"
     else:self.grade="Failed"
     print ("Result:", self.grade) 
#Main Program
r=int (input("Enter Roll Number:"))
n=input ("Enter Name:")
c=input ("Enter Course Name:")
m=int (input ("Enter Marks:"))
#creating the object
print("Result")
studl=Result() 
studl.getdata(r,n,c)
studl.getMarks (m)
studl.displaystudent()
studl.displayMarks()
studl.calculateGrade() 
        