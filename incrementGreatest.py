def incrementLargeby1(digits):
    temp = 0
    index = 0
    for i in range(0, len(digits)):
        if digits[i] > temp:
            temp = digits[i]
            index = i
    temp = temp + 1
    digits[index] = temp
    return digits

print(incrementLargeby1([8,2,1]))
