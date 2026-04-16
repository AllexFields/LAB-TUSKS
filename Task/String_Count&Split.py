# count parameters---start parameter(by default starts from 0)

name=input("Enter a word: ")
k=name.count("a",0)    #count -- it counts the occurrence. Two parameters - 'variable' & 'starting position'
print(k)
s=name.split(" ",maxsplit=-1)      #maxsplit -- no of splits we want...default -1 means no limit
print(s)