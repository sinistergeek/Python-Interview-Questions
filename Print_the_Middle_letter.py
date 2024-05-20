def middle_letter(string):
    if len(string) % 2 == 0:
        return ''
    middle_index = len(string) // 2
    letter = string[middle_index]
    return letter
letter = middle_letter('hello')
print(letter)
