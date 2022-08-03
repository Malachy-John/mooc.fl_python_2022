# Write your solution here

from operator import truediv


def anagrams(word_one, word_two):

    word_one = sorted(word_one)
    word_two = sorted(word_two)

    if(word_one == word_two):
        return True
    else:
        return False