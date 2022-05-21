'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

#LeetCode Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx=-1
        for i in range(len(haystack)):
            if needle[0]==haystack[i] and i+len(needle)-1<len(haystack):
                if haystack[i:i+len(needle)]==needle:
                    return i
        return -1
