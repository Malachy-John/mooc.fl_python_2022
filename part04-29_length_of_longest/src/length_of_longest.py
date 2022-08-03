# Write your solution here
def length_of_longest(list_one):
    longest = 0

    for word in list_one:
        length = len(word)
        print(length)
        if length > longest:
            longest = len(word)
    return longest

