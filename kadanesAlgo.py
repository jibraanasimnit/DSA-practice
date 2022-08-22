A = [1,5,6,-1,2,3]
for i in range(0, len(A)):
    for j in range(i, len(A)):
        for k in range(i, j):
           print(A[k], end=" ")
        print("\n")
    print("\n")
    
           