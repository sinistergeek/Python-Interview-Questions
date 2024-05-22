lst = [1,0,2,0,4,0,6,5]
for number in lst:
    if number == 0:
        lst.remove(number)
        lst.append(number)

print(lst)
