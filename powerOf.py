def powerOf(base, power):
    if  power == 0 :
        return 1
    else:
        return  base*powerOf(base, power-1)
print(powerOf(7, 2))