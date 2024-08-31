"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])


sol = Solution()
# Example 1: Output: 5
s = "Hello World"

print(sol.lengthOfLastWord(s=s))

# Example 2: Output: 4
s = "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s=s))


# Example 3: Output: 6
s = "luffy is still joyboy"
print(sol.lengthOfLastWord(s=s))
