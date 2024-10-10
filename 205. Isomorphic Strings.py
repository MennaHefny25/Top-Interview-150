"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 

while preserving the order of characters. 

No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = zip(s,t)

        map_s_t = {}
        map_t_s = {}
        for s_char, t_char in l:

            if s_char in map_s_t:
                if map_s_t[s_char] != t_char:
                    return False
            else:
                map_s_t[s_char] = t_char
            
            if t_char in map_t_s:
                if map_t_s[t_char] != s_char:
                    return False
            else:
                map_t_s[t_char] = s_char

        return True
    


# check if there is a one-directional map exist from 's' to 't'

sol = Solution()
# Example 1: Output: true
s = "egg"
t = "add"

print(sol.isIsomorphic(s=s, t=t))


# Example 2: Output: false
s = "foo"
t = "bar"



print(sol.isIsomorphic(s=s, t=t))

# Example 3: Output: true
s = "paper"
t = "title"

print(sol.isIsomorphic(s=s, t=t))



