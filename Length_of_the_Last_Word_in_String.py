def length_of_last_word(sentence):
    words_list = sentence.split(' ')
    result = len(words_list[-1])
    if words_list[-1].endswith('.'):
        result -= 1

    print(result)

length_of_last_word('i love programming')
