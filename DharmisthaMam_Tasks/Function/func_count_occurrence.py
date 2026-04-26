# a function that accepts a string and a character, and returns the number of times the character appears in the string

def count_character(string, char):
    return string.count(char)

word=input("Enter any word: ")
char=input("Enter the character you want to count: ")
print(f"{char} occurs {count_character(word,char)} times")