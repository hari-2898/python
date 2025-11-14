class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    # Overload the < operator
    def __lt__(self, other):
        return self.area() < other.area()


# Taking inputs
l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))
r1 = Rectangle(l1, w1)

l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))
r2 = Rectangle(l2, w2)

# Comparison
if r1 < r2:
    print("Rectangle 1 has smaller area than Rectangle 2")
else:
    print("Rectangle 1 has greater or equal area than Rectangle 2")
