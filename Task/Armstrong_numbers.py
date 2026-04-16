# 4)To check if a number is Armstrong No 


user_num=int(input("Enter a number: "))
if user_num<0:
    print("Negative numbers are not accepted.\nConcept of Armstrong No is only valid for positive integers.")
else:

    count=0
    original=user_num
    new=user_num
    while user_num!=0:
        rem=user_num%10
        user_num=user_num//10
        count+=1
    i=0
    ans=0
    while original!=0:
        rem1=original%10
        original=original//10
        product=rem1**count
        ans+=product
        i+=1
    if ans==new:
        print(f"{new} is an Armstrong Number.")
    else: print(f"{new} is not an Armstrong Number.")