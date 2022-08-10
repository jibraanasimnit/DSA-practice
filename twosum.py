


# arr = [2,5,6,7,8]
# num = 11
# limit = len(arr)
# start = 0
# for i in range(0, limit):
#     if num > (arr[limit] + arr[start]):
#         limit = limit - 1
#     if num < (arr[limit] + arr[start]):
#         start = start + 1
#     if num == (arr[limit] + arr[start]):
#         print(limit, start)

def sumPairs(nums, target):
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)
            
nums = [1,5,6,7,12,31]
sumPairs(nums, 37)
            
