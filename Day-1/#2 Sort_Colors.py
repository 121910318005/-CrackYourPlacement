'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Use Dutch National Flag Algorithm
        l, mid, h = 0, 0, len(nums)-1
        while mid<=h:
            if nums[mid]==0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[h], nums[mid] = nums[mid], nums[h]
                h-=1
        return nums
'''
Dutch National Flag Algorithm is used to sort array containing [0, 1, 2]

Time complexity: O(N), where N is the number of elements in the array, as we sort the array in a single traversal only.
Space complexity: O(1), as no extra space is required.
'''


Below Approach is not recommended.
'''
#Leet code
# Naive Approach(Not recommended)
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


