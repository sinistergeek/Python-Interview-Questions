def same_subsequent(string):
    for i in range(0,len(string)):
        if string[i] == string[i+1]:
            return string[i]
letter = same_subsequent('hello')
print(letter)
