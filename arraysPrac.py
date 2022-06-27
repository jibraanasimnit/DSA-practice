# # from array import array


# A = [[1,2], [3,4], [5,7], [1,2]]
# print(A[1][0])
# A.append([7,8])
# print(A)
# A.insert(0, [0,0])
# print(A)
# A.extend([[79]])
# print(A)
# A.remove([79])
# print(A)
# A.pop()
# print(A)
# print(A.index([1,2]))
# # A.tostring()
# print(A.count([1,2]))

# print(A[1:3])


import numpy as np
twod_array = np.array([[11,12,97,89], [34,21,81,12], [12,21,98,10], [21,22,19,11]])
# print(twod_array)
# newtwod_array = np.insert(twod_array, 0, [69,69,69,69], axis = 0)
# print(newtwod_array)
newtwod_array = np.append(twod_array, [69,69,69,69], axis = 0)
print(newtwod_array)
