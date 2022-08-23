#UNORDERED
#has erorrs

def moveZeroes(nums):
        last = len(nums)-1
        for i in range(0, len(nums)-2):
            if len(nums) < 2:
                return nums
            elif nums[i] == 0:
                zeroIndex = i
                temp = nums[last]
                nums[zeroIndex] = temp
                nums[last] = 0
                last = last - 1 
        print(nums)       
moveZeroes([1,2,4,0,0,5])