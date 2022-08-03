# Write your solution here

def no_shouting(my_list):
    list_new = []
    for word in my_list:
        if not word.isupper():
            list_new.append(word)
    return list_new
