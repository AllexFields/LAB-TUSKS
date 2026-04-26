# a function that accepts a list of integers and returns the second largest number in the list

def sec_largest(lst):
    lst.sort(reverse=True)     #reverse=True --> arranges in descending order
    return lst[1]              #fetches element at index pos  1 ---> second largest in lst after being sort

lst=[12,43,22,75,84]
print("Second largest integer is",sec_largest(lst))