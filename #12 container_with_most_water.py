'''
#Leet code
#Solved using 2 pointer approach.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_cap = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         if min(height[i], height[j])*(j-i)>max_cap:
        #             max_cap = min(height[i], height[j])*(j-i)
        # return max_cap
        l, r = 0, len(height)-1
        max_cap = min(height[l], height[r])*(r-l)
        while l<r:
            cap = min(height[l], height[r])*(r-l)
            max_cap = max(cap, max_cap)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_cap
'''
