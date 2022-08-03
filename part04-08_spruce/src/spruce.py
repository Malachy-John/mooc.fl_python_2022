# Write your solution here
def line(num_spaces, num_chars):
    print(" " * num_spaces, end="")
    print("*" * num_chars)

def spruce(tiers):
    print("a spruce!")
    index = 0
    star_count = 1
    spaces = tiers - 1
    while index < tiers:
        line(spaces, star_count)
        star_count+=2
        index+=1
        spaces-=1
    line(tiers-1, 1)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)