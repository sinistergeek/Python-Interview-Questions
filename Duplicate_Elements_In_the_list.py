my_list = [2,'python',5,7,'python','java',5]
my_set = set(my_list)
repeated_elements = []
for element in my_set:
    if my_list.count(element) > 1:
        repeated_elements.append(element)

print(repeated_elements)
