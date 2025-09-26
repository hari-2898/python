# write a program to create a single string separated with space from two strings by swaping the characters at possition 1.
str1=input("enter first string:")
str2=input("enter second string:")
str3=str1.replace(str1[0],str2[0])
str4=str2.replace(str2[0],str1[0])
print(str3+" "+str4)
