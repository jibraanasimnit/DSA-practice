num = 12
arr = []
i = 1
while i*i <= num:
    
    if num%i == 0:
        arr.append(i)
        if num//i != i:
            arr.append(num//i)
    i = i+1
print(arr)