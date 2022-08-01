# # # from array import array


# # A = [[1,2], [3,4], [5,7], [1,2]]
# # print(A[1][0])
# # A.append([7,8])
# # print(A)
# # A.insert(0, [0,0])
# # print(A)
# # A.extend([[79]])
# # print(A)
# # A.remove([79])
# # print(A)
# # A.pop()
# # print(A)
# # print(A.index([1,2]))
# # # A.tostring()
# # print(A.count([1,2]))

# # print(A[1:3])


import numpy as np
twod_array = np.array([[11,12,97,89], [34,21,81,12], [12,21,98,10], [21,22,19,11]])
# newtwod_array = np.insert(twod_array, 1 ,[[6,9,6,9]], axis=0)

# def access_elements(array, row_index, col_index):
#     if row_index >= len(newtwod_array) and col_index >= len(newtwod_array[0]):
#         ping('incorrect')

# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(twod_array) & colIndex >= len(twod_array[0]):
#         print('wrong size')
#     else:
#         print(twod_array[rowIndex][colIndex])
# accessElements(twod_array, 0, 2)
def traversal():
        for i in range(len(twod_array)):
            for j in range(len(twod_array[0])):
                # print(twod_array[i][j])
                if twod_array[i][j] == 98:
                    print('num found! at row index', i, 'and col index', j)
# traversal()

def deleteInArray(rowIndex):
    newTwoDarray = np.delete(twod_array, rowIndex, axis=0)
    print(newTwoDarray)
deleteInArray(0)



