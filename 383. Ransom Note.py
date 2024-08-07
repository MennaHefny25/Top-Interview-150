"""
Given two strings ransomNote and magazine, 

return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_count, magazine_count = Counter(ransomNote), Counter(magazine)

        return ransomNote_count & magazine_count == ransomNote_count
        

sol = Solution()
# Example 1: Output: false
ransomNote = "a"
magazine = "b"

print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))



# Example 2: Output: false
ransomNote = "aa"
magazine = "ab"

print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))

# Example 3: Output: true
ransomNote = "aa"
magazine = "aab"

print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))



