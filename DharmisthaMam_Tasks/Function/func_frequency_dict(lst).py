# a function that accepts a list and returns a dictionary where the keys are the elements of the list, 
# and the values are the count of how often each element appears

def create_frequency_dict(lst):
    dictionary={}
    count=0
    emp_lst=[]
    for i in lst:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    return dictionary

lst=[12,14,12,1,65,14]
print(create_frequency_dict(lst))