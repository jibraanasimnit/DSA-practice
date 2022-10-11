# # def practice(A):
# #     target = 12
# #     start = 0
# #     end = len(A)-1
# #     for i in range(0, len(A)-1):
# #         if A[start] + A[end] > target:
# #             end -= 1
# #         elif A[start] + A[end] < target:
# #             start += 1
# #         elif A[start] + A[end] == target:
# #             print(A[start], A[end])
# #             break
# # nums = [1,3,5,6,9]
# # practice(nums)


# # nums = [1,2,2,8,8,9,11,11,11,12,12,12,12]
# # a = 0
# # trigger = 0
# # z = len(nums)-1
# # for i in range(len(nums)-1):
# #     if nums[a] != nums[a+1]:
# #         a += 1
# #     elif nums[a] == nums[a+1]:
# #         if a+1 == len(nums)-1:
# #             trigger += 1
# #             nums[a] = nums[a+1]
# #             nums.pop(a+1)
# #         else:
# #             trigger += 1
# #             nums[a] = nums[a+1]
# #             nums.pop(a+1)
# # print(nums)
# n = 91
# sum = 0
# target = 0
# second = 0

# while(n%10 != 0 & target < 9999999999999999999999):
#     target += 1
#     sum = (n%10)*(n%10)+ sum
#     n = n//10
#     print(sum)
#     if n < 9:
#         second += 1
#         if second == 2:
#             n = sum
#             sum = 0
#             second = 0

from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next 
    def __str__(self):
        values = [str(x.value) for x in self]
        return '-->'.join(values)
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next 
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
            
           
        
        
        

            

