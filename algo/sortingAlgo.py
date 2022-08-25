# # #bubble sort

# # A = [1.0, 1, 6 ,11, 110]

# # temp = 0
# # for i in range(0,  len(A)-1):
# #     for j in range(0, len(A)-1-i):
# #         if A[j] > A[j+1]:
# #             A[j+1], A[j] = A[j], A[j+1]

# # print(A)


# #Selection sort


# A = [19,1,20,11]
# for i in range(0, len(A)):
#     min_index = i
#     for j in range(i+1, len(A)):
#         if A[min_index] > A[j]:
#             min_index = j
#     A[i], A[min_index] = A[min_index], A[i]
# print(A)



#insertion sort

from pydoc import cli


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 & key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)
        
cList = [9,1,2,3,4,5,6,7,8]
insertionSort(cList)
    
         