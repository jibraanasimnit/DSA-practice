def powerOfTwo(n = 5):
    if(n==0):
        return 1;
    else:
        power = powerOfTwo(n-1)
        print(power)
        return power*2
        
print(powerOfTwo(n=5))

    
