# Write your solution here


while True:
    editor_name = input("Editor: ")
    if editor_name.lower() == "word" or editor_name.lower() == "notepad":
        print("awful")
    elif editor_name.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")