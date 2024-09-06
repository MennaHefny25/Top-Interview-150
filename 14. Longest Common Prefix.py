"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


sol = Solution()
# Example 1: Output: "fl"
strs = ["flower","flow","flight"]

print(sol.longestCommonPrefix(strs=strs))

# Example 2: Output: ""
strs = ["dog","racecar","car"]

print(sol.longestCommonPrefix(strs=strs))
