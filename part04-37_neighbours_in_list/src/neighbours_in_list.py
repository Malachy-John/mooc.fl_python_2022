# Write your solution here

def longest_series_of_neighbours(list):
    longest_series = []
    temp_hold = []
    count = 0
    temp_count = 0
    end_of_list = len(list) -2
    for i in range(0, len(list)-1):
            
        if temp_count == 0:
                temp_hold.append(list[i])
                temp_count+=1
        difference = list[i] - list[i+1]
        if difference < 0:
            difference *= -1

        if difference == 1 or difference == 0:      
            temp_hold.append(list[i+1])
            temp_count+=1
            if i == end_of_list:
                if temp_count > count:
                    longest_series = temp_hold
                    count = temp_count
                
        elif difference > 1 or i == end_of_list:
            print(i)
            if temp_count > count:
                longest_series = temp_hold
                count = temp_count
            temp_hold = []
            temp_count = 0
            
            

        
        
    return longest_series

my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]

print(longest_series_of_neighbours(my_list))
