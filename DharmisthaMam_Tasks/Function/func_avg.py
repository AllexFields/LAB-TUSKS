# a function that accepts a list of numbers and returns the average of the numbers

def avg_num(lst):
    sum=0
    for i in lst:
        sum+=i
    ans=sum/len(lst)
    print(f"Avg of the numbers in {lst} is {ans}")
lst_num=[1,2,3,4,5]
avg_num(lst_num)