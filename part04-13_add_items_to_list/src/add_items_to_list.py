# Write your solution here
list_of_values = []
num_of_items = int(input("How many items: "))
index = 0
while index < num_of_items:
    value = int(input(f"Item {index + 1}: "))
    list_of_values.append(value)
    index+=1
print(list_of_values)
