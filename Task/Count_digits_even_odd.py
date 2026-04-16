# No of digits, count of even/odd digits

num=int(input("Enter a number: "))
if num<0:
    num*=-1       # a -ve no throws exception/breaks our code
original_num=num
even=0
digit=0
odd=0
sum=0
while num!=0:
    rem=num%10
    digit+=1
    if rem%2==0:
        even+=1
        sum+=rem
    else:
        odd+=1
        sum+=rem
    num=num//10
print(f"No of odd digits --- {odd}")
print(f"No of even digits --- {even}")
print(f"No of total digits --- {digit}")
