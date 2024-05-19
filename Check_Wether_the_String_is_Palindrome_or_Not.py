def is_palindrome(text):
    rev_text = text[::-1]
    if text == rev_text:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

text = 'hannah'
is_palindrome(text)
