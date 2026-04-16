# Prime Number --- with For Loop


num=int(input("Enter a number: "))
if num<=1:
    print(f"{num} is invalid.Input shall be greater than 1.")

else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime no.")
            break
    else: print(f"{num} is a prime no.")  