class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self): 
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): 
        return 3.14 * self.radius * self.radius

s1 = Square(4)
c1 = Circle(3)

print(s1.area()) 
print(c1.area())
