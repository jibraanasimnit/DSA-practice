def decToBinary(n):
    if n == 0 :
        return 0
    else:
        return n%2 + 10*decToBinary(int(n/2))
print(decToBinary(30))
    