def thousand_seperator(number):
    number = str(number)[::-1]
    separated = ''
    for i in range(0,len(number)):
        if i% 3 == 0 and i != 0:
            separated += ','
        separated += number[i]
    return separated[::-1]
result = thousand_seperator(100000)
print(result)
