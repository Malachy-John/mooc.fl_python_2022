# Write your solution here

def sum_of_positives(list):
    sum = 0

    for number in list:
        if number > 0:
            sum += number
    return sum


