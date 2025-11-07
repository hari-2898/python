class rectangle :
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        print("area=",area)
    def perimeter(self):
        perimeter=2*(self.length + self.breadth)
        print("perimeter=",perimeter)
l=float(input("enter the length :"))
b=float(input("enter the breadth :"))
rect=rectangle()
rect.getdata(l,b)
rect.area()
rect.perimeter()