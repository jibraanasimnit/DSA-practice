nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
i = 0
j = 0
k = m+n-1

while m > 0 and n > 0:
    if nums1[m-1] < nums2[n-1]:
        nums1[k] = nums2[n-1]
        k -=1
        n -= 1
    elif nums1[m-1] > nums2[n-1]:
        nums1[k] = nums1[m-1]
        k-=1
        m -=1
        print(nums1)
if n > 0:
    nums1[k] = nums2[n-1]
    n -= 1
    k -= 1
print(nums1)
              
        
    