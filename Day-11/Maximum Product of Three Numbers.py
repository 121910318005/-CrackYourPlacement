'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
'''

#Leetcode solution
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        else:
            nums.sort()
            if nums[-1]*nums[-2]*nums[-3]>nums[0]*nums[1]*nums[-1]:
                return nums[-1]*nums[-2]*nums[-3]
            else:
                return nums[0]*nums[1]*nums[-1]
