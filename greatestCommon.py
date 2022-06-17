def greatestCommon(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, 'the number is not integer'
    if n1 < 0:
        n1 = -1*n1
    if n2 < 0:
        n2 = -1*n2

    if(n2 == 0):
        return n1
    else:
        return greatestCommon((n2), (n1 % n2))


print(greatestCommon(48, 18))
