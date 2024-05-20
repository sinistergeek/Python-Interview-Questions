def count_vowels_and_consonants(string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char.isspace():
            continue
        else:
            consonant_count += 1

    print('Vowels: ' + str(vowel_count))
    print('Consonants: ' + str(consonant_count))

string = 'A quick brown fox jumps over the lazy dog'
count_vowels_and_consonants(string)
