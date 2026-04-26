# Count Even and Odd Numbers from given range

lower_limit=int(input("Enter lower limit of range: "))
upper_limit=int(input("Enter upper limit of range: "))
count_even=0
count_odd=0
for i in range(lower_limit,upper_limit+1):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"No of odd numbers in range {lower_limit}-{upper_limit} is {count_odd}")
print(f"No of even numbers in range {lower_limit}-{upper_limit} is {count_even}")