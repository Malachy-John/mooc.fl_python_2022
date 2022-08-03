# Copy here code of line function from previous exercise and use it in your solution
def line(num, char):
    print(char * num)
def shape(tri_num, tri_char, sqr_num, sqr_char):
    index = 1
    while index <= tri_num:
        line(index, tri_char)
        index+=1
    index_sqr = 0
    while index_sqr < sqr_num:
        line(tri_num, sqr_char)
        index_sqr+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")