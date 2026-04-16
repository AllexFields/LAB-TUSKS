# create func for checking if a no is prime or not

def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

number=int(input("Enter number: "))
check_prime(number)
