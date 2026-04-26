# a function that accepts a string and a sub-string, and returns True if sub-string 
# found in the string, otherwise False
 
def check_sub_str(string,substr):
    if substr in string:
        return True
    
user_inp=input("Enter a string: ")
check_substring=input("Enter substring you want to search: ")
print(check_sub_str(user_inp,check_substring))
