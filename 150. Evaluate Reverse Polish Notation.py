"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

# class Solution(object):
#     def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         stack = []
#         operators = "+-*/"

#         for token in tokens:
#             if token in operators:
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 if token == '+':
#                     stack.append(num1 + num2)
#                 elif token == '-':
#                     stack.append(num1 - num2)
#                 elif token == '*':
#                     stack.append(num1 * num2)
#                 elif token == '/':
#                     # Integer division in Python 3
#                     stack.append(int(num1 / num2))
#             else:
#                 stack.append(int(token))

#         return stack.pop()

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def resolves(a, b, operator):
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '*':
                return a * b
            elif operator == '/':
                # Use int() to ensure truncation towards zero
                return int(a / b) if a * b >= 0 else -(-a // b)

        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                integer2 = stack.pop()
                integer1 = stack.pop()
                resolved_ans = resolves(integer1, integer2, token)
                stack.append(resolved_ans)
            else:
                stack.append(int(token))
        
        return stack.pop()


sol = Solution()
# Example 1: Output: 9
tokens = ["2","1","+","3","*"]

print(sol.evalRPN(tokens=tokens))

# Example 2: Output: 6
tokens = ["4","13","5","/","+"]

print(sol.evalRPN(tokens=tokens))

# Example 3: Output: 22
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(sol.evalRPN(tokens=tokens))

