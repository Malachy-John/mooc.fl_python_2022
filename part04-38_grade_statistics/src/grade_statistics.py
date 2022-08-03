# Write your solution here
def pass_check(totals):
    passes = 0
    for number in totals:
        if number >= 15:
            passes+=1
    return (passes/len(totals)) * 100

def number_of_stars(grade, totals):
    count = 0
    for number in totals:
        if grade == 5 and number > 27:
            count+=1
        elif grade == 4 and number > 23 and number < 28:
            count+=1
        elif grade == 3 and number > 20 and number < 24:
            count+=1
        elif grade == 2 and number > 17 and number < 21:
            count+=1
        elif grade == 1 and number > 14 and number < 17:
            count+=1
        elif grade == 0 and number >= 0 and number < 15:
            count+=1
    return count
            

def grades_star(totals):
    grade = 5
    for i in range(1, 7):
        count = number_of_stars(grade, totals)
        print(f"  {grade}: {'*' * count}")
        grade-=1       

user_input = " "
number_list = []
totals = []
total = 0
while(user_input!=""):
    user_input = input("Exam results and exercises completed: ")
    if(user_input != ""):
        numbers = user_input.split(" ")
        numbers[0] = int(numbers[0])
        numbers[1] = int(numbers[1])
        number_list.append(numbers)

for number in number_list:
    total += (number[1]//10) + number[0]

    if number[0] < 10:
        totals.append(0)
    else:
        totals.append((number[1]//10) + number[0])

average = total/len(number_list)  

pass_percentage = pass_check(totals)

print("Statistics: " )
print(f"Points average: {average}")
print(f"Pass percentage: {pass_percentage:.1f}")
print(f"Grade distribution: ")
grades_star(totals)


# input 20 100

