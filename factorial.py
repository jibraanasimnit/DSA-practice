from math import factorial


def fact(n):
    assert n >= 0 and int(n) == n, 'no. must be a positive integer'
    if n==0:
        return 1
    else:
        
        factorial = fact(n-1)
        return factorial*n
        

print(fact(10))