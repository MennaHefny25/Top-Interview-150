"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 

12 is written as XII, which is simply X + II. 

The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 

However, the numeral for four is not IIII. Instead, the number four is written as IV. 

Because the one is before the five we subtract it making four. 

The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numeric_map = {
        "I": 1,
        "X": 10,
        "V":5,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }

        # Case `I` before `V` & `X`
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # Case `X` before `L` & `C`
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # Case `C` before `D` & `M`
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        total = 0
        for roman_symbol in s:
            total += roman_numeric_map[roman_symbol]

        return total





sol = Solution()

# Example 1: Output: 3
s = "III"
print(sol.romanToInt(s=s))


# Example 2: Output: 58
s = "LVIII"
print(sol.romanToInt(s=s))



# Example 3: Output: 1994
s = "MCMXCIV"
print(sol.romanToInt(s=s))



