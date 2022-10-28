arr = [-1,-2,-1,-2,-11]
i = 0
low = 0
mid = 1
high = 2
save = -999
while(high<len(arr)):
    i += 1
    one = arr[low]
    two = arr[mid]
    three = arr[high]
    temp = one+two+three
    low = mid
    mid = high
    high += 1

    if temp > save:
        save = temp
print(save)
        
    
