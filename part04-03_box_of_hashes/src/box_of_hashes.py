# Copy here code of line function from previous exercise
def line(num, char):
    print(char * num)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    index = 0
    while index < height:
        line(10, "#")
        index+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
