def bulls_and_cows(secret,guess):
    bulls, cows = 0,0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1

        else:
            if secret[i] in guess:
                cows += 1

    print(f'{bulls}A{cows}B')

secret = '1807'
guess = '7810'
bulls_and_cows(secret,guess)
