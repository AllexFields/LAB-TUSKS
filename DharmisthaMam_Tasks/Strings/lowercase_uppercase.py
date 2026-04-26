# Accept a string from the user and print it in uppercase if the length of the string is greater than 5, 
# else print it in lowercase using a function

def strng_length(inp):
    if len(inp)>5:
        print(inp.upper())
    else:
        print(inp.lower())
user_input=input("Enter a string: ")
strng_length(user_input)
