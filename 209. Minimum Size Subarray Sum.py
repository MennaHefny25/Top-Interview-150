"""
Given an array of positive integers nums and a positive integer target, 

return the `minimal length` of a 

subarray: A subarray is a contiguous non-empty sequence of elements within an array.

`whose sum is greater than or equal to target`. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left_ptr =  0
        curr_window_sum = 0
        min_subarray_len = float('inf')

        for right_ptr in range(len(nums)):
            curr_window_sum +=nums[right_ptr]

            while curr_window_sum >= target:
                min_subarray_len = min(min_subarray_len, right_ptr - left_ptr + 1)
                
                curr_window_sum -= nums[left_ptr]
                left_ptr +=1

        return min_subarray_len if min_subarray_len != float('inf') else 0


sol = Solution()
# Example 1: Output: 2
target = 7
nums = [2,3,1,2,4,3]

print(sol.minSubArrayLen(target=target, nums=nums))

# Example 2: Output: 1
target = 4
nums = [1,4,4]
print(sol.minSubArrayLen(target=target, nums=nums))

# Example 3: Output: 0
target = 11
nums = [1,1,1,1,1,1,1,1]
print(sol.minSubArrayLen(target=target, nums=nums))


