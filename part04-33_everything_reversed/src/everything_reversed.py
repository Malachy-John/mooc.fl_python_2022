# Write your solution here
def everything_reversed(list):
    backward_list = []
    for word in list:
        backward_word = word[::-1]
        backward_list.append(backward_word)

    back_again_list = backward_list[::-1]

    return back_again_list
