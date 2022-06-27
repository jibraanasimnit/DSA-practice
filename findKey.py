A = [5,6,8,9,10]
key = 9
l = 0
h = -1
mid = (A[l] + A[h])//2

while(key != mid):
    mid = (A[l] + A[h])//2
    if key == mid:
        print(mid)
            
    elif key < mid:
        h = h-1
    elif key > mid:
        l = l + 1
        
        
        
    
