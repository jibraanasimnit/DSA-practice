# #bubble sort

# A = [1.0, 1, 6 ,11, 110]

# temp = 0
# for i in range(0,  len(A)-1):
#     for j in range(0, len(A)-1-i):
#         if A[j] > A[j+1]:
#             A[j+1], A[j] = A[j], A[j+1]

# print(A)


#Selection sort

import math


A = [19,1,20,11]
for i in range(0, len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
print(A)
         