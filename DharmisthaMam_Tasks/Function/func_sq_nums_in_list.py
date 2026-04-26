# a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list

def sq_num(num):
    lst_sq=[]
    for i in num:
        lst_sq.append(i**2)
    return lst_sq


user_inp=input("Enters numbers with space: ").split()
lst_num=[]
for i in user_inp:
    lst_num.append(int(i))
print("New list with squares of numbers:",sq_num(lst_num))