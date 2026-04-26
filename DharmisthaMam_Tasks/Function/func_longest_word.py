# a function that accepts a sentence and returns the longest word in the sentence 
# that accepts a sentence and returns the longest word in the sentence

def longest_word(sentence):
    words=sentence.split()
    return max(words,key=len)

sentence="I am Allex Fields"
print(longest_word(sentence)) 

