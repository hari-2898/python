#program to add ING at the end of the given string (length should be at least 3 )if given string is already ing then add "ly"
s = input("enter the string: ")
length = len(s)
if length > 2:
    if s[-3:] == 'ing':
        s+= 'ly'
    else:
        s+= 'ing'

print("new style string:", s)
