array = [7,88,6,3,11]

biggestNo = array[0]

for index in range(0, len(array)):
    if array[index] > biggestNo:
        biggestNo = array[index]
        
print(biggestNo)