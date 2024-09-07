"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 

compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""




class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        trapped_water = 0 

        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i]) 

        for i in range(len(height)):
            trapped_water += min(max_left[i], max_right[i]) - height[i]

        return trapped_water


sol = Solution()
# Example 1: Output: 6
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(sol.trap(height=height))


# Example 2: Output: 9
height = [4,2,0,3,2,5]

print(sol.trap(height=height))