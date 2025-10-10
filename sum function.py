#sum of two numbers using function 
def sum(a, b):
    total = a + b
    return total

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
s = sum(a, b)
print("Sum of two numbers:", s)
