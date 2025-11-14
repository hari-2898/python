class Shape:
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

def show_perimeter(shape):
        print("Perimeter:",shape.perimeter())

rect = Rectangle(10, 5)
circle = Circle(3)
square = Square(6)
show_perimeter(rect)  
show_perimeter(circle)  
show_perimeter(square)
