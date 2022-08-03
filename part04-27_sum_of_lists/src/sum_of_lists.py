# Write your solution here
def list_sum(list_one,list_two):
    list_total = []

    for i in range(0, len(list_one)):
        sum = list_one[i] + list_two[i]
        list_total.append(sum)
    return list_total

#print(list_sum([1,2,3],[1,2,3]))