# a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by 2 & 3 both

def check_div(lst):
    new_lst=[]
    for i in lst:
        if i%2==0 and i%3==0:
            new_lst.append(i)
    return new_lst

lst_nums=[21,4,6,12,15,24,27]
print("New list with only numbers divisible by 2 & 3 --->",check_div(lst_nums))