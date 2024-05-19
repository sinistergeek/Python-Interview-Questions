def find_majority_element(num_list):
    for i in num_list:
        count = num_list.count(i)
        if count > len(num_list) // 2:
            return i

numbers = [1,7,8,7,7,7]
result = find_majority_element(numbers)
print(result)
