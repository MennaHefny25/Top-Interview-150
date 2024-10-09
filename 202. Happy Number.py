"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Helper function to calculate the sum of the squares of digits of a number
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10  
                total_sum += digit ** 2  
                number = number // 10  
            return total_sum  
        
        seen = set()  # Create a set to track numbers we've already seen to detect cycles
        
        # Continue the process until n becomes 1 (happy number) or a cycle is detected
        while n != 1 and n not in seen:
            seen.add(n)  
            n = get_next(n)  
        
        return n == 1


sol = Solution()
# Example 1: Output: true
n = 19

print(sol.isHappy(n=n))

# Example 2: Output: false
n = 2

print(sol.isHappy(n=n))