"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move the top boundary down by 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left by 1

            # Traverse from right to left along the bottom row (if still within bounds)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up by 1
            
            # Traverse from bottom to top along the left column (if still within bounds)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right by 1

        return result


sol = Solution()
# Example 1: Output: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(sol.spiralOrder(matrix=matrix))

# Example 2: Output: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(sol.spiralOrder(matrix=matrix))