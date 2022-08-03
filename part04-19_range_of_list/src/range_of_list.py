# Write your solution here
def range_of_list(a_list):
    min = a_list[0]
    max = a_list[0]

    for i in range(1, len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
        elif a_list[i] < min:
            min = a_list[i]
    difference = max - min
    return difference

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = range_of_list(my_list)
    print(result)