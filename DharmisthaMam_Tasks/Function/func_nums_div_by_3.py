# a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3

def div_3(lst):
    new_list=[]
    for i in lst:
        if i%3==0:
            new_list.append(i)
    return new_list

lst=[12,32,13,9]
print("New list with only numbers divisible by 3 --->",div_3(lst))