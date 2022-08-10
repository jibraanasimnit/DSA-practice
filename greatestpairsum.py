arr = [3,5,6,7,8,9,10]
test = 0
for i in arr:
    for j in arr:
        if i == j:
            continue
        if i + j > test:
            test = i+j
            pair = str(i) + ',' + str(j)
print('sum is :' + str(test) , 'for pair:', str(pair))