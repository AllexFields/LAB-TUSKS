# All numbers Divisible by 5 & 7 between the range given by user

l=int(input("Enter Lower limit of your desired range: "))
if l>=35:
    u=int(input("Enter Upper limit of your desired range: "))
    i=l  
    while i<=u:
        if i%5==0 and i%7==0:
            print(f"{i} is divisible by 5")
        i+=1
else: print("Lower limit can't be less than 35")