

myDict = {"name":"Edy", "age": 26,"address":"london"}

# # def searchDict(dict, value):
# #     for key in dict:
# #         if dict[key] == value:
# #             print(key, value) 
# #     print('The value does not exist')
# # (searchDict(myDict, 26))

# # myDict.pop("age")
# # print(myDict)

# # myDict.clear()

# # print(myDict)

# newDict = myDict.copy()
# # print(newDict)

for i in myDict:
    newNewDict = {}.fromkeys([1,2,3], myDict[i])
    print(newNewDict)
    
# ranDict = {"name":"jibraan"}
# (myDict.update(ranDict))
# print(myDict)

# if 'name' in myDict:
#     # print(True)
    
# for key in myDict:
#     # print(key)

# num_dict = {'a' : 1, 'b' : 2, 'c' : 3}
# value = 1

# for  i in num_dict:
#     value = value*num_dict[i]
# print(value)

# keys = ['a', 'b', 'c', 'd']
# values = [1,2,3,4]
#                                             #ZIP KEY VALUE PAIRS IN A DICT
# new_dict = dict(zip(keys,values)) 
# print(new_dict)


from optparse import Values
import string


# string_given = "my name is name alpha alpha"
# split_string = string_given.split()
# d = {}
# for i in split_string:
#     if i not in d.keys():
#         d[i] = 0
#     d[i] = d[i] + 1
# print(d)
        
def dict_from_list(keys, values):
    d = {}
    for i in range(0, len(keys)):
        d[keys[i]] = values[i]
    return d
keys = [1,2,3,4,5]
values  = [0,9,8,7,6]

square_dict = {}
def square_keys(keys):
    for i in range(0, len(keys)):
        square_dict[keys[i]] = keys[i]*keys[i]
    return square_dict
print(square_keys(keys))