# Write your solution here

item_list = []
item = -1

while item !=0:
    item = int(input("New item: "))
    if item != 0:
        item_list.append(item)
        print(f"The list now: {item_list}")
        print(f"The list in order: {sorted(item_list)}")
    elif item ==0:
        print("Bye!")
    
        


#print(f"You typed in {len(item_list)} different items")