def counter(string):
    alphabets = 0
    digits = 0
    symbols = 0

    for char in string:
        if char.isalpha():
            alphabets += 1
        if char.isdigit():
            digits += 1
        if not char.isalnum():
            symbols += 1

    print(f'Alphabets: {alphabets}')
    print(f'Digits: {digits}')
    print(f'Symbols: {symbols}')

counter('Hello123.')
