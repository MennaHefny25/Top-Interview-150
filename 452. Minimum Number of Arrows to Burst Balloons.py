"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. 

The balloons are represented as a 2D integer array points where 

points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end. 

You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 

A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. 

There is no limit to the number of arrows that can be shot. 

A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort points by end  
        points.sort(key=lambda x: x[1])

        min_arrows = 1 # at least one arrow needed
        
        prev_end = points[0][1]

        for ballon in points[1:]:
            if prev_end < ballon[0]:
                    # No overlap another arrow needed
                    min_arrows +=1
                    # Update the prev_end variable to the end coordinate of the current balloon.
                    prev_end = ballon[1]
        
        return min_arrows


sol = Solution()

# Example 1: Output: 2
points = [[10,16],[2,8],[1,6],[7,12]] # [[1,6], [2,8], [7,12], [10,16]]

print(sol.findMinArrowShots(points=points))

# Example 2: Output: 4
points = [[1,2],[3,4],[5,6],[7,8]]

print(sol.findMinArrowShots(points=points))

# Example 3: Output: 2
points = [[1,2],[2,3],[3,4],[4,5]]

print(sol.findMinArrowShots(points=points))