# Write your solution here

from sqlite3 import IntegrityError


list_values = [1, 2, 3, 4, 5]

user_entry = 0

while(user_entry != -1):
    user_entry = int(input("Index: "))

    if(user_entry!= -1):
        new_value = int(input("New value:"))
        list_values[user_entry] = new_value
        print(list_values)
