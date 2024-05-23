def first_and_last(num_list, target_element):
    first = None
    last = None
    for index, num in enumerate(num_list):
        if num == target_element:
            if first == None:
                first = index
            last = index
    return first, last
numbers = [1, 5, 6, 7, 8, 2, 7, 9, 1]
target = 7
result = first_and_last(numbers, target)
print(result)
