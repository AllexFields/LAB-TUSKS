# a Python program that uses `map()` to add a given number to each element in a list. 
# Input: `[1, 2, 3, 4]`, `5` Output: `[6, 7, 8, 9]`

lst_numbers=[12,1,3,4,5]
user_inp=int(input("Enter number you want to add in each number of list: "))
print(list(map(lambda x:x+user_inp,lst_numbers)))