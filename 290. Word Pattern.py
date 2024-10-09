"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 

Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        words_to_chars, chars_to_words = {}, {}

        for char, word in zip(pattern, words):
            #  Check if char is already mapped to a different word
            if char in chars_to_words:
                if chars_to_words[char] != word:
                    return False
                
            # Check if word is already mapped to a different char
            if word in words_to_chars:
                if words_to_chars[word] != char:
                    return False
                
            chars_to_words[char] = word
            words_to_chars[word] = char

        return True


sol = Solution()
# Example 1: Output: true
pattern = "abba"
s = "dog cat cat dog"

print(sol.wordPattern(pattern=pattern, s=s))

# Example 2: Output: false
pattern = "abba"
s = "dog cat cat fish"

print(sol.wordPattern(pattern=pattern, s=s))

# Example 3: Output: false
pattern = "aaaa"
s = "dog cat cat dog"

print(sol.wordPattern(pattern=pattern, s=s))