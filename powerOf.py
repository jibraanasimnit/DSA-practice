def powerOf(base, power):
    assert power >= 0 and int(power) == power, 'power must be non-negative integer'
    if  power == 0 :
        return 1
    else:
        return  base*powerOf(base, power-1)
print(powerOf(7, -2))