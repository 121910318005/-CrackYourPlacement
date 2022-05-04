'''
#Leet code solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1]^nums[i]==0:
                return nums[i]
 '''             

nums = list(map(int, input().split(' ')))
nums.sort()
for i in range(1, len(nums)):
  if nums[i-1]==nums[i]:
    print(f'Duplicate number is: {nums[i]}')
    break
else:
  print('Duplicate number not found')
