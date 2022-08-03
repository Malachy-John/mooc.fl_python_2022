def square_of_letters(layers:int):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max_length = (layers * 2) - 1
    letter_choice = layers - 1
    start_col = 0
    end_col = max_length
    before_start = 0
    after_end = 1
    letters_string = ""
    rows_of_letters = []

    for row in range(layers):
        for column in range(max_length):
            if column in range(start_col, end_col):
                letters_string += alpha[letter_choice - row]
            elif column < start_col:
                letters_string += alpha[letter_choice - before_start]
                before_start+=1
            elif column >= end_col:
                letters_string += alpha[letter_choice - row + after_end]
                after_end +=1
            
        rows_of_letters.append(letters_string)
        letters_string=""
        after_end = 1
        before_start = 0
        start_col +=1
        end_col -= 1

    for i in range(len(rows_of_letters)):
        print(rows_of_letters[i])
        
    rows_of_letters.reverse()

    for i in range(1, len(rows_of_letters)):
        print(rows_of_letters[i])



layers = int(input("Layers: "))

square_of_letters(layers)

