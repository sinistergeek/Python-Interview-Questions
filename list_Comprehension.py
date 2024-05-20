fruits = ['apple','banana','pineapple','mango','watermelon']
c_fruits = [fruit for fruit in fruits if fruit[0] not in 'aeiouAEIOU']
print(c_fruits)
