# Write your solution here
def distinct_numbers(list_one):
    list_sorted = sorted(list_one)
    end = len(list_sorted) -1
    list_support =[]
    

    

    for i in range(0, end):
        if list_sorted[i] != list_sorted[i +1]:
            list_support.append(list_sorted[i])
        if i == end-1:
            list_support.append(list_sorted[end])
    return list_support

#print(distinct_numbers([9,8,7,6,9,8,7,6,10,3,3,3,3,1]))