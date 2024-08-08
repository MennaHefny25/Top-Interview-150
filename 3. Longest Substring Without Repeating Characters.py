"""
Given a string s, find the length of the longest 

`substring`:  A substring is a contiguous non-empty sequence of characters within a string.

without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_ptr = 0
        sub_str_set = set()
        max_window_len = 0

        for right_ptr in range(len(s)):
            # check for repeated chars
            while s[right_ptr] in sub_str_set:
                # repeated char found
                sub_str_set.remove(s[left_ptr])

                # advance left pointer 
                left_ptr +=1

            sub_str_set.add(s[right_ptr])

            max_window_len = max(max_window_len, right_ptr - left_ptr + 1)

        return max_window_len

sol = Solution()
# Example 1: Output: 3
s = "abcabcbb"

print(sol.lengthOfLongestSubstring(s=s))

# Example 2: Output: 1
s = "bbbbb"
print(sol.lengthOfLongestSubstring(s=s))


# Example 3: Output: 3
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s=s))




