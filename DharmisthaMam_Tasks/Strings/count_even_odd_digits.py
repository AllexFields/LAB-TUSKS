# Count no of even and odd digits from given number

num_input=int(input("Enter a number: "))
original=num_input
count_even=0
count_odd=0

while num_input!=0:
    digit=num_input%10
    if digit%2==0:
        count_even+=1
    else:
        count_odd+=1    
    num_input=num_input//10
print(f"{original} has {count_even} even digits")
print(f"{original} has {count_odd} odd digits")