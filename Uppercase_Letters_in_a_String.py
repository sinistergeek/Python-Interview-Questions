def uppercase_Index(string):
    index_list = []
    for index,letter in enumerate(string):
        if letter.isupper():
            index_list.append(index)
    return index_list

indexes = uppercase_Index('heLLo')
print(indexes)
