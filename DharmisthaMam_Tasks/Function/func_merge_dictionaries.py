#  a function that accepts two dictionaries and returns a single dictionary that contains the merged key-value pairs from both dictionaries

def merge_dicts(dict1, dict2):
    new_dict={}
    for k,v in dict1.items():
        new_dict[k]=v
    for k,v in dict2.items():
        new_dict[k]=v
    return new_dict              # in case of same keys, second dictionary overwrites the first one

dict1={"name":'Astha','age':21,'city':'Delhi'}
dict2={'name':'Shivam','job':'DA','salary':24567}
print(merge_dicts(dict1,dict2))


# Or we can use update method.....to merge two dictionaries

