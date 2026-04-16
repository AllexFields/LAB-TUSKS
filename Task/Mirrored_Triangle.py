# Mirrored Triangle

num=int(input("Enter number: "))
for i in range(1,num+1):
    for j in range(num-i,0,-1):
        print(" ", end=" ")
    for j in range(i):
         print("*",end=" ")
    print()