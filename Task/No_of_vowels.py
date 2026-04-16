# count no of vowels in each city ----- try counting vowels by using index

lst_city=['Ajmer','Bhopal','Ooty','Thiruvananthapuram','Karnataka']
for i in lst_city:
    count=0
    for j in range(0,len(i)):
        if i[j] in 'aeiou':
            count+=1
    print(f"{i}--->{count}") 


