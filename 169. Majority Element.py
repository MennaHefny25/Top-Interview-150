"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


from collections import Counter
import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = math.ceil(len(nums) / 2)
        nums_count = Counter(nums)
        for num, count in nums_count.items():
            if count > majority_element:
                majority = num

        return majority

sol = Solution()
# Example 1: Output: 3
nums = [3,2,3]
print(sol.majorityElement(nums=nums))

# Example 2: Output: 2 
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums=nums))

