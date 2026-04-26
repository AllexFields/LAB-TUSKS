# a string from the user and print it in uppercase if the length of the string is greater than 5, 
# else print it in lowercase using a function

def uppercase(name):
    if len(name)>5:
        print(name.upper())
    else:
        print(name.lower())

strng=input("Enter a name: ")
uppercase(strng)