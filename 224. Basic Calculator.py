"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 positive, -1 negative
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in "+-":
                current_result += sign * current_number
                current_number = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push the result and sign onto stack
                stack.append(current_result)
                stack.append(sign)
                # Reset for new expression
                current_result = 0
                sign = 1
            elif char == ')':
                # Complete the current expression
                current_result += sign * current_number
                current_number = 0
                # Pop sign and previous result from stack
                current_result *= stack.pop()  # This is the sign before '('
                current_result += stack.pop()   # This is the result before '('

        # Final addition for any remaining number
        return current_result + sign * current_number

sol = Solution()
# Example 1: Output: 2
s = "1 + 1"

print(sol.calculate(s=s))

# Example 2: Output: 3
s = " 2-1 + 2 "

print(sol.calculate(s=s))

# Example 3: Output: 23
s = "(1+(4+5+2)-3)+(6+8)"

print(sol.calculate(s=s))