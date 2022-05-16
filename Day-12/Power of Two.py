'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
'''

#Solution 1
from math import *
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            p = math.log(n, 2)
            if int(p) == float('%.9f'%p):
                return True
            else:
                return False
                
#Solution 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return n&(n-1)==0
