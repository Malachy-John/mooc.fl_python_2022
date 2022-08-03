# Write your solution here

def formatted(list):
    new_list = []
    for number in list:
        new_num = f"{number:.2f}"
        new_list.append(new_num)
    return new_list

