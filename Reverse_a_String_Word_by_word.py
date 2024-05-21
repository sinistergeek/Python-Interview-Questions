def reverse_by_word(sentence):
    words_list = sentence.split(' ')
    reversed_words_list = words_list[::-1]
    result = ' '.join(reversed_words_list)
    print(result)

reverse_by_word('this is blue')
