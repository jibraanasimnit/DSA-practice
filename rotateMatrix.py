import numpy as np

myArray = np.array[[1,2,3], [4,5,6], [7,8,9]]

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(0,n//2):
        first = layer
        last =  n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i-1][layer]