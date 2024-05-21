def odd_factor_sum(number):
    factors = []
    for i in range(1,number):
        if number % i == 0:
            factors.append(i)

    sum = 0
    for i in factors:
        if i % 2 != 0:
            sum += i
    print(sum)

num = 18
odd_factor_sum(num)
