def sumOfN(n):
    if n == 1:
        return 1
    else:
        return n+sumOfN(n-1)
print(sumOfN(10))


