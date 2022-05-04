'''
#Leet code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            if nums[i-1]^nums[i]==0:
                del nums[i]
            else:
                i+=1
'''

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        res=1
        temp.append(nums[0])
        for i in range(1, len(nums)):
            if (nums[i]^temp[res-1])!=0:
                temp.append(nums[i])
                res+=1
        for i in range(res):
            nums[i]=temp[i]
        del temp
        return res
'''

nums = list(map(int, input().split(' ')))
temp = []
count = 1
temp.append(nums[0])
for i in range(1, len(nums)):
  if (nums[i]^temp[count-1])!=0:
    temp.append(nums[i])
    count+=1
for i in range(res):
  nums[i] = temp[i]
del temp
print(f'k = {count}, nums = {nums}')
