'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def LongestCommonPrefix(s):
  c = ""
  m = min(s) #min string length stored in m
  for i in range(m):
    p = s[0][i]
    for j in range(len(s)):
      if s[j][i]!=p:
        return c
    c+=p
  return c

s = input('Enter any string to get common prefixes: ')
print('Common Prefix is: ',LongestCommonPrefix(s))
