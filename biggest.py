# write a program to accept three numbers from user and find the biggest number.
num1=float(input("enter the first number: "))
num2=float(input("enter the second number"))
num3=float(input("enter the third nuber"))
if(num1>num2) and (num2>num3):
      largest = num1
elif(num2>num1) and (num2>num3):
      largest = num2 
else:
      largest = num3 
print("the largest number is",largest)
              
    