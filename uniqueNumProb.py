N = int(input('enter the size of array : '))
array = []
j = 0
while(len(array)<N):
    array.append(input("enter the array element: ").format(j))
tempArray = []
for i in range(0, len(array)):
    if array[i] not in tempArray:
        tempArray.append(array[i])
print(tempArray)