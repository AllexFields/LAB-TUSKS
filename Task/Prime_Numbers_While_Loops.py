# Prime Number --- with While Loop

num=int(input("Enter a number: "))
if num<=1:
    print(f"{num} is an invalid input. Input should be greater or equal to 2.")
else:
    i=2
    while i<num:
        if num%i==0:
            print(f"{num} isn't a prime no.")
            break
        i+=1       
    else:
        print(f"{num} is a prime no.")