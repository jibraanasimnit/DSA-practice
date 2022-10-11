# def practice(A):
#     target = 12
#     start = 0
#     end = len(A)-1
#     for i in range(0, len(A)-1):
#         if A[start] + A[end] > target:
#             end -= 1
#         elif A[start] + A[end] < target:
#             start += 1
#         elif A[start] + A[end] == target:
#             print(A[start], A[end])
#             break
# nums = [1,3,5,6,9]
# practice(nums)


# nums = [1,2,2,8,8,9,11,11,11,12,12,12,12]
# a = 0
# trigger = 0
# z = len(nums)-1
# for i in range(len(nums)-1):
#     if nums[a] != nums[a+1]:
#         a += 1
#     elif nums[a] == nums[a+1]:
#         if a+1 == len(nums)-1:
#             trigger += 1
# #             nums[a] = nums[a+1]
# #             nums.pop(a+1)
# #         else:
# #             trigger += 1
# #             nums[a] = nums[a+1]
# #             nums.pop(a+1)
# # print(nums)
# n = 18
# target = 0
# second = 0
# sum = 0

# while(target < 999999999999999999999999):
#     target += 1
#     sum = (n%10)*(n%10)+ sum
#     n = n//10
#     print(sum)
#     if sum == 1:
#         print('true')
#     if n < 9:
#         second += 1
#         if second == 2:
#             n = sum
#             sum = 0
#             second = 0


            
n = 8
target = 0
second = 0
sum = 0

while( target < 999):
    target += 1
    sum = (n%10)*(n%10)+ sum
    n = n//10
    
    if n < 9:
        second += 1
        if second == 2:
            print(sum)
            if sum == 1:
                print('True')
            n = sum
            sum = 0
            second = 0
    
        