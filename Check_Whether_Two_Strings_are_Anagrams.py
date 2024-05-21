def is_anagram(str1,str2):
    str1.replace(' ','')
    str2.replace(' ','')

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        print('The two strings are anagrams')

    else:
        print('The two strings are not anagrams')


is_anagram('listen','silent')
