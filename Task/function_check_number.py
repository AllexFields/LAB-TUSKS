# create a func that prints whether a no is pos+,-ve or zero

def check_num(num):
    if num>0:
        print(f"{num} is positive")
    elif num<0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")
num=int(input("Enter a number: "))
check_num(num)