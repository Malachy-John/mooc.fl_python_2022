# Write your solution here

def longest(strings: list):
    longest_value = 0
    longest_word = ""
    for word in strings:
        if len(word) > longest_value:
            longest_value = len(word)
            longest_word = word
    return longest_word



