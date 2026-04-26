# a program to check all list elements are alphabetics or not

lst=['jungle','leopard',12]
for i in lst:
    if type(i)!=str:
        print("All elements are not alphabetic")
        break
    elif type(i)==str:
        if i.isalnum()==True:
            print("All elements are not alphabetic")
            break
else:
    print("All elements are  alphabetic")