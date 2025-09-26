# write a program to generate fibonacci series of n items
n=int(input("enter the  number of n items : "))
f1=0
f2=1
sum=0 
count=1
print("fibonacci series of n terms: ",end=" ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    f1=f2
    f2=sum
    sum=f1+f2
    