def find_sum(nums_list):
    sum = 0

    for i in nums_list:
        sum += i
    return sum

nums_list = [5,6,7,8,23,51]
sum = find_sum(nums_list)
print(sum)
