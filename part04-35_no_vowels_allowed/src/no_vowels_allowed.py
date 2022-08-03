# Write your solution here

def no_vowels(my_string):
    new_string = ""
    for letter in my_string:
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
            new_string += letter
    return new_string
   
