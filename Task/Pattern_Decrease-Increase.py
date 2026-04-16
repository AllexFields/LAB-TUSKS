# Decrease-increase pattern

num=int(input("Enter a number: "))
for i in range(1,num*2):     #no of rows---if num=5 then rows=5*2-1=9
    if i<=num:
        for j in range(num+1,i,-1):
            print("*", end=" ")
        print()
    else:
        for j in range(i-num+1):
            print("*", end=" ")
        print()