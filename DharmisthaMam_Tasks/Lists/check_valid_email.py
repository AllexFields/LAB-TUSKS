# A program to check if a list of strings is a valid list of email addresses

lst=['aastha@gmail.com','shivam@gmail.com','abhishek@gmail','ritesh.com@gmail']

for i in lst:
    if i.endswith('@gmail.com')==False:
        print("Given list contains invalid email(s)")
        break
else:
    print("Given list contains valid email(s)")
