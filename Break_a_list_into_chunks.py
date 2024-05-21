numbers = [2,3,6,7,3,5,7,8,9,2,20,24,16,17,23,19]
chunks = []

for i in range(0,len(numbers),4):
    chunk = numbers[i:i+4]
    chunks.append(chunk)

for j in chunks:
    print(j)
