# a function that accepts a string and counts how many vowels are in the string

def count_vowel(name):
    count=0
    for i in name:
        if i in 'aeiou':
            count+=1
    return count

word=input("Enter a word: ")
print("No of vowels",count_vowel(word))