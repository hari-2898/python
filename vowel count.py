#program to form a string of vowels,selected from a given string
list=input("enter the string:")
vowels=['a','e','i','o','u',"A","E","I","O","U"]
vowel_list=[]
for list in list:
    if list in vowels:
        vowel_list.append(list)
print("vowels:",vowel_list)        

