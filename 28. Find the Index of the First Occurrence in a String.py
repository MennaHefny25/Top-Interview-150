"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 

or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

import re 
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        first_occurrence_idx = re.search(needle,haystack)
        
        return first_occurrence_idx.start() if first_occurrence_idx != None else -1

sol = Solution()
# Example 1: Output: 0
haystack = "sadbutsad"
needle = "sad"

print(sol.strStr(haystack=haystack, needle=needle))

# Example 2: Output: -1
haystack = "leetcode"
needle = "leeto"

print(sol.strStr(haystack=haystack, needle=needle))