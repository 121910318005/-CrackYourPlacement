'''
#Leet code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
            else:
                c+=1
        for i in range(c):
            temp.append(0)
        for i in range(len(temp)):
            nums[i]=temp[i]
        del temp
'''
