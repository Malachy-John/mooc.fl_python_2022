# Write your solution here
def same_chars(text, pos_1,pos_2):
    if pos_2 >= len(text) or pos_1 >= len(text):
        return False
    if text[pos_1] == text[pos_2]:
        return True
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("codor", 0, 3))