# Write your solution here
def mean(a_list):
    length_list = len(a_list)
    total = 0
    for i in range(0, len(a_list)):
        total += a_list[i]
    return total/len(a_list)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)