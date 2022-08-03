# Write your solution here

number = int(input("Please type in a positive integer: "))

neg_num = number * -1

for i in range(neg_num, number+1):
    if i != 0:
        print(i)
