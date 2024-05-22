def sort_alphabets(string):
    new_string = ''
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(int(char))
        else:
            new_string += char

    new_string = sorted(new_string)
    new_string = ''.join(new_string)
    sum_numbers = sum(numbers)
    final_string = new_string + str(sum_numbers)
    print(final_string)

sort_alphabets('9python123')
