# a function that accepts a list of strings and returns the longest string in the list

def longest_word(lst):
    lst.sort(key=len)
    return lst[len(lst)-1]

lst=['akash','vyom','aastha']
print(f"Longest string is \'{longest_word(lst)}\'")
