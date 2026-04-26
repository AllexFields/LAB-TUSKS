# a function that accepts a number and checks if it is an Armstrong number

def check_armstrong_no(num):
    if num<0:
        print("Negative numbers are not accepted.\nConcept of Armstrong No is only valid for positive integers.")
    else:

        digi=0
        original=num
        new=num
        while num!=0:       # to count digits --- len isn't applicable to int values
            rem=num%10
            num=num//10
            digi+=1
        sum=0
        while original!=0:
            rem1=original%10
            original=original//10
            sq=rem1**digi
            sum+=sq
        if sum==new:
            print(f"{new} is an Armstrong Number.")
        else: print(f"{new} is not an Armstrong Number.")

    

user_input=int(input("Enter a number: "))
check_armstrong_no(user_input)
