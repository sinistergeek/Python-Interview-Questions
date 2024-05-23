def kth_largest_element(nums_list,k):
    loop_timer = k - 1
    unique_numbers = list(set(nums_list))
    while loop_timer >  0:
        current_maxium = max(unique_numbers)
        unique_numbers.remove(current_maxium)
        loop_timer -= 1
    kth_largest = unique_numbers[-1]
    print(kth_largest)

numbers = [2,3,1,5,6,4]
k = 3 
kth_largest_element(numbers,k)
