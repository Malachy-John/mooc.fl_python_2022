# Write your solution here

list_of_values = []
user_in = ""

list_index = 0

while user_in != "x":
    list_index +=1
    print(f"The list is now {list_of_values}")
    user_in = input("a(d)d, (r)emove or e(x)it:")

    if user_in == "d":
        list_of_values.append(list_index)
    elif user_in == "r":
        list_of_values.remove(list_index -1)
        list_index -=2
    elif user_in == "x":
        print("Bye!")
    
