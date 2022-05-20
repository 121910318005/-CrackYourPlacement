'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

#Leetcode solution
class Solution:
    def column_matrix(self, t, matrix):
        r = t[0]
        c = t[1]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i==r:
                    matrix[i][j]=0
                if j==c:
                    matrix[i][j]=0
        return matrix

    def setZeroes(self, matrix: List[List[int]]) -> None:
        l=[] #new list is created for storing the row & column values where zeroes are there
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.append((i, j)) #Row index, column index are stored in the list in the form of the tuple.
        for i in range(len(l)):  #Based on the list which contains row indexes and column indexes, operation is performed one by one.
            matrix = self.column_matrix(l[i], matrix)

#Same approach as above code, but changing the way of solving (makes efficient code)
class Solution:
    def zerofy(self,p,matrix):
        matrix[p[0]] = [0] * len(matrix[0])  #matrix[p[0]] represents list[tuple[0]]
        for i in range(len(matrix)):
            matrix[i][p[1]] = 0
        return matrix
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    pos.append((i,j))
        for i in pos:
            self.zerofy(i,matrix)
