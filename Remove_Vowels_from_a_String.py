def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char

    print(new_string)

string = 'A quick brown fox jumps over the lazy dog'
remove_vowels(string)
