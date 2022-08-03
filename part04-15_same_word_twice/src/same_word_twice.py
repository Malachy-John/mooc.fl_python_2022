# Write your solution here

word_list = []
word =""

while True:
    word = input("Word: ")
    if word not in word_list:
        word_list.append(word)
    elif word in word_list:
        break

print(f"You typed in {len(word_list)} different words")