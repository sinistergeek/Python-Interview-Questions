def encrypt(character):
    if character == 'z':
        secret = 'a'
    elif character == 'Z': 
        secret = 'A'
    else:
        secret = chr(ord(character) + 1)
    return secret 

def main_runner(string):
    result = ''
    for character in string:
        if character.isalpha():
            result += encrypt(character)
        else:
            result += character
    return result 

encrypted = main_runner('I am lazy')
print(encrypted) 

encrypted = main_runner('I AM LAZY')
print(encrypted)
