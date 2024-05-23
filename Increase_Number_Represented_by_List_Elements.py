def add_one(digits):
    digits[-1] += 1
    carry = digits[-1] // 10
    digits[-1] = digits[-1] % 10
    for i in range(len(digits) -2,-1,-1):
        if carry:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
    if carry:
        digits.insert(0,carry)

    return digits

digits = [8,9,9]
added_digits = add_one(digits)
print(added_digits)
