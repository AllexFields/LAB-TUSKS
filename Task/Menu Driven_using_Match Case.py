# Menu-Driven Program --- match_case inside a loop

while True:
    print(f"1. Factorial\n2. Count Digit\n3. Sum of Digits\n4. Prime Number\n5. Exit")
    # print("\n1. Factorial")
    # print("\n2. Count Digit")
    # print("\n3. Sum of Digits")
    # print("\n4. Prime Number ")
    # print("\n5. Exit")
    choice=int(input("Enter choice: "))
    match choice:
        case 1:
            num=int(input("Enter number "))
            fact=1
            for i in range(1,num+1):
                fact*=i
            print(f"Factorail of {num} is {fact}")
        case 2:
            num=int(input("Enter number: "))     #if user enters something like '1234rte56' how to count digits while leaving letters?
            count=0
            num1=num
            while num!=0:
                rem=num%10
                count+=1
                num=num//10
            print(f"{num1} contains {count} digits")
        case 3:
            num=int(input("Enter number: "))
            ans=num
            sum=0
            while num!=0:
                rem=num%10
                sum+=rem
                num=num//10
            print(f"Sum of digits of {ans} is {sum}")
        case 4:
            num=int(input("Enter number: "))
            for i in range(2,num):
                if num%i==0:
                    print(f"{num} isn't a Prime Number")
                    break
            else:
                print(f"{num} is a prime number")

        case 5:
            break
        case _:
            print("Invalid Choice ")
