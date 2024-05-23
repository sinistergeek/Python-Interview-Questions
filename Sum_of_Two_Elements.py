def find_sum(numbers,target):
    temp_list = []
    for i in numbers:
        if(target - i ) in temp_list:
            print(target - i,i)

        temp_list.append(i)

numbers = [1,5,6,3,2,4]
target_sum = 7
find_sum(numbers,target_sum)
