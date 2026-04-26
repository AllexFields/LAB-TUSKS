# a function that accepts a list of strings and returns a new list with only the strings that have an odd length

def lst_odd(lst):
    new_lst=[]
    for i in lst:
        if len(i)%2!=0:
            new_lst.append(i)
    return new_lst

lst=['aastha','shivam','vyom','suraj']
print(lst_odd(lst))