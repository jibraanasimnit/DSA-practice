def decToBinary(num):
    if (num == 0):
        return 1
    else:
        return decToBinary((num/2)%2)

print(decToBinary(13))