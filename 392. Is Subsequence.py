"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from 

the original string by deleting some (can be none) of the characters 

without disturbing the relative positions of the remaining characters. 

(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

# 1st solution
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        ptr_s = 0

        for element in t:
            if element == s[ptr_s]:
                ptr_s +=1

            if ptr_s == len(s):
                break

        return ptr_s == len(s)

# 2nd solution
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        it = iter(t)
        return all(char in it for char in s)

sol = Solution()
# Example 1: Output: true
s = "abc"
t = "ahbgdc"

print(sol.isSubsequence(s, t))
print(sol.isSubsequence(s, t))


# Example 2: Output: false
s = "axc"
t = "ahbgdc"

print(sol.isSubsequence(s, t))
print(sol.isSubsequence(s, t))



# 1st sol

# ptr_s = 0

# for element in t:
#     if element == s[ptr_s]:
#         ptr_s +=1

#     if ptr_s == len(s):
#         break

#     r = ptr_s == len(s)

# print(r)
    