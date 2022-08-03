# Write your solution here
from ctypes import string_at


string_val = input("Please type in a string: ")

for character in string_val:
    print(character)
    print("*")