arr = [12,2,-3,-4,5,6,-1,1]

def printFirstNegativeInteger( A, N, K):
    ans = []
    for i in range(0,N-K+1):
        if K > 1 and N > 1:
            for j in range(i, i+K):
                if A[j] < 0:
                    ans.append(A[j])
                    break
                elif j == i+K-1:
                    ans.append(0)
        elif A[i]>0:
            ans.append(0)
        else:
            ans.append(A[i])
    return ans
        

        
