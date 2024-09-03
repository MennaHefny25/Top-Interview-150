"""
Given an integer array nums, return an array answer such that answer[i] is equal 

to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        postfix = 1
        out = [1] * (len(nums))

        for i in range(1, len(nums)):
            out[i] = out[i-1] * nums[i-1]
            
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]
        return out



sol = Solution()
# Example 1: Output: [24,12,8,6]
nums = [1, 2, 3, 4]

print(sol.productExceptSelf(nums=nums))

# Example 2: Output: [0,0,9,0,0]
nums = [-1, 1, 0, -3, 3]

print(sol.productExceptSelf(nums=nums))
