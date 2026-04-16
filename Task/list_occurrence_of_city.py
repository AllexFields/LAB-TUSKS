# which city occurs how many times in a list?

lst_city=['Ajmer','Bhopal','Ooty','Ajmer','Thiruvananthapuram','Bhopal','Ajmer','Karnataka']
count=[]    # to stop repetitons of same values of i 
for i in lst_city:
    if i not in count:
        print(f"{i} ----> {lst_city.count(i)}") 
        count.append(i)