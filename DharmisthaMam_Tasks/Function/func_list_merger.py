# a function that accepts two lists of equal length and merges them into a dictionary 
# where the keys are the indices (0 to n-1) and the values are the elements from both lists

def merge_lists_into_dict(lst1, lst2):
    dictionary={}
    for i in range(0,len(lst1)):
        dictionary[i]=lst1[i],lst2[i]      
    return dictionary

lst1=['anshul','rashmi','shyam']
lst2=['aastha','shivam','roshni']
print(merge_lists_into_dict(lst1,lst2))