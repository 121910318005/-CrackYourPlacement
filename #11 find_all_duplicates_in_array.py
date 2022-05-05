#Leet code
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     key = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j]<nums[key]:
        #             key=j
        #     nums[i], nums[key] = nums[key], nums[i]
        nums.sort()
            
        dup =[]
            
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                dup.append(nums[i])
        return dup
