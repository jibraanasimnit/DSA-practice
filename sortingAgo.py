#bubble sort

A = [12, 1, 6 ,11, 110]

temp = 0
for i in range(0,  len(A)-1):
    for j in range(0, len(A)-1-i):
        if A[j] > A[j+1]:
            A[j+1], A[j] = A[j], A[j+1]

print(A)