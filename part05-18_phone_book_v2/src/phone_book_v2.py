# Write your solution here

def search(phone_book: dict, phone_name: str):
    if len(phone_book) == 0:
        return "no number"
    if phone_name not in phone_book:
        return "no number"
    else:
        for person in phone_book:
            if person == phone_name:
                string_val = ""
                for i in range(len(phone_book[phone_name])):
                    
                    #print("we made it here")
                    #print(len(phone_book[phone_name]))
                    #print(phone_book[phone_name][i])

                    string_val += phone_book[phone_name][i]

                    string_val += "\n"


                return string_val

def add(phone_book: dict, phone_name: str, phone_number: str):
    if phone_name not in phone_book:
        phone_book[phone_name] = []
    phone_book[phone_name].append(phone_number)
    return "ok!"

phone_book = {}
    
command = -1
while(command != 3):
    command = int(input("command(1 search, 2 add, 3 quit: "))
    if command != 3:
        if command == 1:
            name = input("name:")
            print(search(phone_book, name))
        elif command == 2:
            new_name = input("name: ")
            new_num = input("number: ")
            print(add(phone_book, new_name, new_num))
    else:
        print("quitting...")
        #print(phone_book)


