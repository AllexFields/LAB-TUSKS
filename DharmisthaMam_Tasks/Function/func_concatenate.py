# a function that accepts a list of strings and a separator string, then returns a new string where all elements of the list are joined using the separator

def concatenate_with_separator(lst, separator):
    new_string=""
    stop=0
    for i in lst:
        new_string+=i
        stop+=1
        if stop<=len(lst)-1:        # stop --- to remove the separator at the end
            new_string+=separator
    return new_string

lst_words=['Aastha','Shivam','Vyom','Kashish','Suraj']
sep_inp=input("Enter separator that you want to join the words: ")
print(concatenate_with_separator(lst_words,sep_inp))