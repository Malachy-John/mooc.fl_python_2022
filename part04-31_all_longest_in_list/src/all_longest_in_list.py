# Write your solution here
def all_the_longest(my_list):
    longest_value = 0
    longest_list = []

    #my_list.sort()

    for word in my_list:
        if len(word) > longest_value:
            longest_value = len(word)
            longest_list = []
            longest_list.append(word)
        elif len(word) == longest_value:
            longest_list.append(word)
        #longest_list.sort()
    return longest_list


