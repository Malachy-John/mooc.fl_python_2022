# Write your solution here
def most_common_character(my_string):
    highest = 0
    highest_letter = ""
    for letter in my_string:
        if my_string.count(letter) > highest:
            highest = my_string.count(letter)
            highest_letter = letter
    return highest_letter

#print(most_common_character("aaabb"))
