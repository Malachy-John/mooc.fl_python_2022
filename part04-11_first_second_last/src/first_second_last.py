# Write your solution here
from os import remove


def first_word(sentence):
    space_first = sentence.find(" ")
    first_word = sentence[:space_first]
    return first_word
def second_word(sentence):
    index = 0
    while index < 1:
        space = sentence.find(" ")
        sentence = sentence[space+1:]
        index +=1
    if " " in sentence:
        sentence = sentence[:sentence.find(" ")]
    else:
        sentence = sentence
    return sentence
def last_word(sentence):
    index = 0
    while " " in sentence: 
        space_first = sentence.find(" ")
        sentence = sentence[space_first+1:]    
        index +=1
    return sentence
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))