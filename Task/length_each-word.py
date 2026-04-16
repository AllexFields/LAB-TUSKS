# length of each word in a string---sentence

sentence=input("Enter a sentence: ")
list_sentence=sentence.split()
emp_lst=[]               
for i in list_sentence:
    if i not in emp_lst:
        print(f"{i} has {len(i)} letters")
        emp_lst.append(i)          # adds each element in empty list one by one making sure only unique values are included