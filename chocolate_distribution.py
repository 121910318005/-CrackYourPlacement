"""
Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. 
There are m students, the task is to distribute chocolate packets such that: 
  Each student gets one packet.
  The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
  
Examples:
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and 
we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum 
difference between maximum and minimum packet 
sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 
Explanation:
The set goes like 3,4,7,9,9 and the output 
is 9-3 = 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50} , m = 7 
Output: Minimum Difference is 10 
Explanation:
We need to pick 7 packets. We pick 40, 41, 
42, 44, 48, 43 and 50 to minimize difference 
between maximum and minimum. 
"""

#Python code

arr = list(map(int, input('Enter array: ').split(' ')))
m = int(input('Enter no.of students: '))
if len(arr)==0 and m==0:
  print('Nothing to share and no one to take')
elif len(arr)<m:
  print('Students are more than packets')
else:
  #Sorting arr, using selection sort
  key = 0
  for i in range(len(arr)):
    key = i
    for j in range(i+1, len(arr)):
      if arr[j]<arr[key]:
        key=j
    arr[i], arr[key] = arr[key], arr[i]
  #arr is sorted
  min_diff = arr[-1]
  for i in range(len(arr)):
    if i+m-1<=len(arr)-1:
      if arr[i+m-1]-arr[i]<min_diff:
        min_diff = arr[i+m-1]-arr[i]
  print('Minimum difference is: ', min_diff)
