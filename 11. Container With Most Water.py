"""
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ptr, right_ptr = 0, len(height) - 1
        max_area = 0

        while left_ptr < right_ptr:
            curr_width = right_ptr - left_ptr
            min_line = min(height[left_ptr], height[right_ptr])
            curr_area = curr_width * min_line

            max_area = max(max_area, curr_area)

            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area



sol = Solution()
# Example 1: Output: 49
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height=height))

# Example 2: Output: 1
height = [1,1]
print(sol.maxArea(height=height))



# left_ptr, right_ptr = 0, len(height) - 1
# max_area = 0

# while left_ptr < right_ptr:
#     curr_width = right_ptr - left_ptr
#     min_line = min(height[left_ptr], height[right_ptr])
#     curr_area = curr_width * min_line

#     max_area = max(max_area, curr_area)

#     if height[left_ptr] < height[right_ptr]:
#         left_ptr += 1
#     else:
#         right_ptr -= 1

# print(max_area)
