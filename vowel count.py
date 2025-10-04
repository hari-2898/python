#program to form a list of vowels,selected from a given list
list=input("enter the string:")
vowels=['a','e','i','o','u']
vowel_list=[]
for list in list:
    if list in vowels:
        vowel_list.append(list)
print("vowels:",vowel_list)        