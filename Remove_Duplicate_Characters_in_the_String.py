def remove_duplicates(string):
    new_string = ''
    for char in string:
        if char not in new_string:
            new_string += char 

    print(new_string)

text1 = '12stars23'
remove_duplicates(text1)
