def selectionSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums
cList = [11,21,9,8]
print(selectionSort(cList))