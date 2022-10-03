
def sumPairs(nums, target):
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)
            
nums = [1,5,6,7,12,31]
sumPairs(nums, 37)
            
