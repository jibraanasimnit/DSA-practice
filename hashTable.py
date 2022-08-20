# class Hashtable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]
#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h = h + ord(char)
#         return h % self.MAX
#     def add(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val
        
# t = Hashtable()
# t.get_hash('march 6')
# t.add('march')
#TWO SUM USING HASHTABLE
nums = [7,1,2,6]
target = 8
hash = {}
for i in range(0, len(nums)):
    complement = target - nums[i]
    if complement not in hash:
        hash[nums[i]] = i
print (hash[complement],nums[i])

#Sub Array with sum zero
    