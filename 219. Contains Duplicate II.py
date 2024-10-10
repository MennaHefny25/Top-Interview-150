"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        l_ptr = 0

        for r_ptr in range(len(nums)):
            if r_ptr - l_ptr > k:
                window.remove(nums[l_ptr])
                l_ptr += 1

            if nums[r_ptr] in window:
                return True
            window.add(nums[r_ptr])

        return False



sol = Solution()
# Example 1: Output: true
nums = [1,2,3,1]
k = 3

print(sol.containsNearbyDuplicate(nums=nums, k=k))

# Example 2: Output: true
nums = [1,0,1,1]
k = 1

print(sol.containsNearbyDuplicate(nums=nums, k=k))

# Example 3: Output: false
nums = [1,2,3,1,2,3]
k = 2

print(sol.containsNearbyDuplicate(nums=nums, k=k))