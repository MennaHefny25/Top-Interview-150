"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_stack = []

        for character in s:
            if character in '([{':
                open_stack.append(character)
            else:
                if not open_stack:
                    return False
                top = open_stack[-1]
                if (character == ')' and top != '(') or \
                   (character == ']' and top != '[') or \
                   (character == '}' and top != '{'):
                    return False
                open_stack.pop()
        return not open_stack

sol = Solution()
# Example 1: Output: true
s = "()"

print(sol.isValid(s=s))

# Example 2: Output: true
s = "()[]{}"

print(sol.isValid(s=s))

# Example 3: Output: false
s = "(]"

print(sol.isValid(s=s))

# Example 4: Output: true
s = "([])"

print(sol.isValid(s=s))
