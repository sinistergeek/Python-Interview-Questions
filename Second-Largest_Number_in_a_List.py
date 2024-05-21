numbers = [51,51,23,6,5,2]
second_largest = 0
numbers.sort(reverse=True)
for i in range(len(numbers)):
    if numbers[i] == numbers[i+1]:
        continue 
    second_largest = numbers[i+1]
    break 
print(second_largest)
