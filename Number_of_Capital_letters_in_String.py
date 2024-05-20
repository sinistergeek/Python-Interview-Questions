def count_capitals(string):
    capital_counter = 0
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            capital_counter += 1
    print(capital_counter)

count_capitals('The Sun emits UV light')
