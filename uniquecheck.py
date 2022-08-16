from hashlib import new


myList = [2,3,4,6,7,7,9]

newList = []
counter = 0
for i in myList:  #o(n)
    if i in newList: #o(1)
        
        
        print(i, counter)
        continue
    
    else:
        newList.append(i)
if len(newList) == len(myList):
    print('all are unique')
else:
    print('non unique elements found.')