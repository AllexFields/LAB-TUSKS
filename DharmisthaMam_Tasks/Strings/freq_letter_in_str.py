# Find frequency of letter from given string

strng=input("Enter any string: ")
count=0
lst=[]
count=0
for i in strng:
    if i not in lst:
        count+=1
        print(f"{i} ---> {strng.count(i)} ")
        lst.append(i)
    