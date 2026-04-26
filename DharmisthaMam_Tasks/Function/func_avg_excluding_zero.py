# a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values

def avg_nonzero(lst):
    total=0
    count=0
    for i in lst:
        if i!=0:
            total+=i       # gives total sum of non-zero nums only
            count+=1       # counts only non-zero nums
    avg=total/count
    return avg

lst_nums=[1,2,0,3,4,5,0]
print("Average of non-zero numbers is", avg_nonzero(lst_nums))