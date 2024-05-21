numbers = [51,51,23,6,5,2]
number_set = set(numbers)
numbers = list(number_set)
max_number = max(numbers)
numbers.remove(max_number)
largest_number = max(numbers)
print(largest_number)
