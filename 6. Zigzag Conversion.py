"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 

(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""

"""
Traversal Logic:

Start at the first row, then move downward row by row until reaching the last row.
Once at the last row, move back up diagonally until the first row is reached, and then repeat.
Maintain an array for each row to collect characters.

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if numRows is 1, return the string as is
        if numRows == 1:
            return s
            
        # Initialize an array of empty strings for each row
        rows = [''] * min(numRows, len(s)) # ensures that the number of rows is never greater than the number of characters in the string.
        
        # Variables to track the current row and the direction (down or up)
        current_row , down =  0, False
        
        # Iterate through each character in the input string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char
            
            # If we're at the first or last row, reverse direction
            if current_row == 0 or current_row == numRows - 1:
                down = not down
            
            # Move to the next row (down or up)
            current_row += 1 if down else -1
        
        # Join all rows together to form the final string
        return ''.join(rows)


sol = Solution()
# Example 1: Output: "PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 3

print(sol.convert(s=s, numRows=numRows))

# Example 2: Output: "PINALSIGYAHRPI"
s = "PAYPALISHIRING"
numRows = 4

print(sol.convert(s=s, numRows=numRows))


# Example 3: Output: "A"
s = "A"
numRows = 1

print(sol.convert(s=s, numRows=numRows))