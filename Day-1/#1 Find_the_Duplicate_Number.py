'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
'''

#Leet code solution
#Below code is not optimal because they asked not to modify the array.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1]^nums[i]==0:
                return nums[i]
              
#Optimal code with O(n) Time complexity, without changing/ modifying the array.
''' Given that array contains numbers within range of 1 to n-1, where n is the length of the array. Here it is 1 <= nums[i] <= n'''
''' So See readme.md file before understanding the solution approach'''
arr = list(map(int, input('Enter array: ').split(' ')))
for i in range(len(arr)):
 idx = arr[i]-1
 if arr[idx]<0:
  print(f'Duplicate Number {idx+1} found at index {i}') 
  break #Since there is only one duplicate number in array, if there are morethan one duplicate elements in array then use extra space to store the numbers.
