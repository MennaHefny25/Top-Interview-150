"""
You are given a string s and an array of strings words. 

All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" 

are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
"""
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Edge case: If `s` or `words` is empty, return an empty list.
        if not s or not words:
            return []
        
        # Initialize variables
        words_occurrence = Counter(words)  # Count occurrences of each word in `words`
        word_length = len(words[0])  # Length of each word
        window_len = word_length * len(words)  # Total length of concatenated words
        n = len(s)
        result = []
        
        # Traverse the string `s` using a sliding window approach
        for i in range(n - window_len + 1):
            # Extract a window of length `window_len`
            current_window = s[i:i + window_len]
            # Split the window into words of length `word_length`
            seen_words = []
            for j in range(0, window_len, word_length):
                seen_words.append(current_window[j:j + word_length])
            
            # Compare the frequency of words in this window with `words_occurrence`
            if Counter(seen_words) == words_occurrence:
                result.append(i)  # Valid start index, append to result
        
        return result


sol = Solution()
# Example 1: Output: [0,9]
s = "barfoothefoobarman"
words = ["foo","bar"]

print(sol.findSubstring(s=s, words=words))

# Example 2: Output: []
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

print(sol.findSubstring(s=s, words=words))

# Example 3: Output: [6,9,12]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print(sol.findSubstring(s=s, words=words))
