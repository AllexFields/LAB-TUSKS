# Write a program to print length of string without len function

string_inp=input("Enter a string: ")
length=0
for i in string_inp:
    length+=1
print(f"Length of {string_inp} is {length}")