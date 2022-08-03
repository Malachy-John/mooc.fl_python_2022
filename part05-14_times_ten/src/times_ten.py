# Write your solution here
from audioop import mul


def times_ten(start_index: int, end_index: int):
    multiple_dict = {}
    for i in range(start_index, end_index+1):
        multiple_dict[i] = i * 10
    return multiple_dict
        



if __name__ == "__main__":
    d = times_ten(3,6)
    print(d)