# 2) Count\Sum total even digits of a number

num=int(input("Enter a number: "))
original_num=num
count=0
sum=0
if num<0:
    num*=-1          #digits are always +ve ~ 0 to 9
while num!=0:
    rem=num%10
    num=num//10
    if rem%2==0:
        count+=1
        sum+=rem
print(f"Sum of even digits is {sum}.")
print(f"No of even digits in {original_num} is {count}")