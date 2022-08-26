from hashlib import new


myList = [2,3,4,6,7,7,9]

newList = []
counter = 0
for i in myList: 
    if i in newList: 
        print(i, counter)
        continue
    
    else:
        newList.append(i)
if len(newList) == len(myList):
    print('all are unique')
else:
    print('non unique elements found.')