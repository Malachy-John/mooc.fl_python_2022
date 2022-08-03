# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):
    word_two = word[::-1]
    if word_two == word:
        return True
    else:
        return False

    
    
while(True):

    words = input("Please type in a palindrome: ")

    if palindromes(words):
        print(f"{words} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

