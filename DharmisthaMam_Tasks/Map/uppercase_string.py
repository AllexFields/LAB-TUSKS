# a Python program that uses `map()` to convert a list of strings to uppercase. 
# Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']


lst_fruits=['apple', 'banana', 'cherry']
print(list(map(lambda x:x.upper(),lst_fruits)))