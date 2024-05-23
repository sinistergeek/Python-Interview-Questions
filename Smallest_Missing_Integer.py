def find_smallest_missing(lst):
    lst.sort()
    for i,_ in enumerate(lst):
        if lst[i] + 1 == lst[i+1]:
            continue
        else:
            return lst[i] + 1

numbers = [2,3,6,-1,5,1,0]
missing_number = find_smallest_missing(numbers)
print(missing_number)
