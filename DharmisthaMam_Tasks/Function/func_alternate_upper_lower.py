# a function that accepts a string and returns the string in alternating uppercase and lowercase characters

def alt_up_low(name):
    new_strng=""             # without an empty string, we get single elements printed in Upper and Lower.
    for i in range(len(name)):
        if i%2==0:
            new_strng+=name[i].upper()
        else:
           new_strng+=name[i].lower()

    return new_strng

name='shivam'
print(alt_up_low(name))


