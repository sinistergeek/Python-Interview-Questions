my_list = [1,3,4,5,6,7,8,9,10]
n = len(my_list)
total = ((n + 1) + (n + 2)) // 2
temp_total = sum(my_list)
missing_number = total - temp_total
print(missing_number)

