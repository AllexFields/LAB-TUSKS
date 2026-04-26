# a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False

def check_email(email):
    # if '@' and '.' in email:        # checks either '@' or '.' one at a time, not both
    if '@' in email and '.' in email:
        return True
    else:
        return False
    
user_inp=input("Enter email address: ")
print(check_email(user_inp))