# a function that accepts two strings and returns the common characters between them

def common_char(str1,str2):
    new_str=""
    for i in str1:
        if i in str2:
            new_str+=i
    return new_str

word1=input("Enter a word: ")
word2=input("Enter another word: ")
print("Common characters in both words are:",common_char(word1,word2))