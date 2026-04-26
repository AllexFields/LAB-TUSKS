# a Python program that uses `map()` to find the length of each string in a list of strings. 
# Input: `['hello', 'world', 'python']` Output: `[5, 5, 6]`

lst_string=['Aastha','Alok','Om','Geetanjali']
print(list(map(lambda x:len(x), lst_string)))