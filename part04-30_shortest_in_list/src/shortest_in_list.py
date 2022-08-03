# Write your solution here
def shortest(list):
    shortest = len(list[0])
    shortest_word = list[0]
    for word in list:
        if len(word) < shortest:
            shortest = len(word)
            shortest_word = word
    return shortest_word
