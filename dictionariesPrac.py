

myDict = {"name":"Edy", "age": 26,"address":"london"}

# def searchDict(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             print(key, value) 
#     print('The value does not exist')
# (searchDict(myDict, 26))

# myDict.pop("age")
# print(myDict)

# myDict.clear()

# print(myDict)

newDict = myDict.copy()
# print(newDict)

for i in myDict:
    newNewDict = {}.fromkeys([1,2,3], myDict[i])
    # print(newNewDict)
    
ranDict = {"name":"jibraan"}
(myDict.update(ranDict))
print(myDict)

if 'name' in myDict:
    print(True)
    
for key in myDict:
    print(key)