'''
#Leet code
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        key=0
        for i in range(len(nums)):
            key = i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[key]:
                    key=j
            nums[i], nums[key] = nums[key], nums[i]
'''

#Approach 1
nums = list(map(int, input().split(' ')))
nums.sort()
print(nums)

'''
Approach 2
using sorting techniques
Bubble sort
Selection sort
Insertion sort
Merge sort
'''
