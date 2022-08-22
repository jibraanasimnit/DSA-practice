# # class Hashtable:
# #     def __init__(self):
# #         self.MAX = 100
# #         self.arr = [None for i in range(self.MAX)]
# #     def get_hash(self, key):
# #         h = 0
# #         for char in key:
# #             h = h + ord(char)
# #         return h % self.MAX
# #     def add(self, key, val):
# #         h = self.get_hash(key)
# #         self.arr[h] = val

# # t = Hashtable()
# # t.get_hash('march 6')
# # t.add('march')
# # TWO SUM USING HASHTABLE
# nums = [7, 1, 2, 6]
# target = 8
# hash = {}
# for i in range(0, len(nums)):
#     complement = target - nums[i]
#     if complement not in hash:
#         hash[nums[i]] = i
# print(hash[complement], nums[i])

# Sub Array with sum zero

nums = [-3, 4, -3, -1, 1]

hashMap = {}
pref_sum = 0

for i in range(0, len(nums)):
    pref_sum = pref_sum + nums[i]
    if pref_sum == 0:
        print('zero')
        
    if pref_sum not in hashMap:
        hashMap[pref_sum] = i
    else:
        print('exists')

         


