"""
Given an array of intervals where 
    intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = []

        # Sort on start of interval
        intervals.sort(key=lambda x: x[0]) 

        prev_interval = intervals[0]

        # Loop over intervals starting from second interval
        for interval in intervals[1:]:
            # Check if the start of current interval <= ending of previous interval
            if interval[0] <= prev_interval[1]:
                prev_interval[1] = max(prev_interval[1], interval[1]) # update ending of interval
            else:
                merged.append(prev_interval)
                prev_interval = interval

        merged.append(prev_interval)

        return merged


sol = Solution()
# Example 2: Output: [[1,6],[8,10],[15,18]]
intervals = [[1,3],[2,6],[8,10],[15,18]]

print(sol.merge(intervals=intervals))

# Example 2: Output: [[1,5]]
intervals = [[1,4],[4,5]]

print(sol.merge(intervals=intervals))