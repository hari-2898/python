#write a program to accept no from user and find factorial
num=int(input("enter the number to find factorial"))
fact=1
if(num<0):
  print("sorry,factorial doesnot exist for negative numbers")
elif(num==0):
  print("the factorial of 0 is 1")
else: 
   for i in range(1,num+1): 
       fact=fact*i
       print("the factorial of the give number",num,"is",fact)      
               