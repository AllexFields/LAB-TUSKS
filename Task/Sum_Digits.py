# 1) Sum of digits of a number

num=int(input("Enter a number: "))
num_original=num
if num<0:
    num*=-1        #digits are always +ve ~ 0 to 9
sum=0
while num!=0:
    rem=num%10
    sum+=rem
    num=num//10
print(f"Sum of digits of {num_original} is {sum}")