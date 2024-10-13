"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
# Syntax error
# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         ranges = []
#         if not nums:
#             return ranges
        
#         start = nums[0]

#         for i in range(1, len(nums) + 1):
#             # Check if the current number is the last element or not consecutive
#             if i == len(nums) or nums[i] != nums[i-1] + 1:
#                 # Single number case
#                 if start == nums[i-1]:
#                     ranges.append(str(start))
#                 else:
#                     ranges.append(f"{start}->{nums[i - 1]}")
                
#                 # Update the start to the current number
#                 if i < len(nums):
#                     start = nums[i]

#         return ranges


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:return [] #Handling the edge case
        ans = []
        start = end  = str(nums[0]) #Initially we will keep the start and end pos and at same 
        for i in range(1 , len(nums)):
            if nums[i] != nums[i - 1] + 1:  #Checking if numbers are bounded 
                if start != end:     #If there exist a incrementing part
                    ans.append(start+'->'+end)
                else:
                    ans.append(start)
                start = end = str(nums[i])
            else:
                end = str(nums[i]) #Increasing the size of the existing bounds
        if start != end: #To handle the remaining elements out of the loop
            ans.append(start+'->'+end)
        else:
            ans.append(start)
        return ans

sol = Solution()
# Example 1: Output: ["0->2","4->5","7"]
nums = [0,1,2,4,5,7]

print(sol.summaryRanges(nums=nums))

# Example 2: Output: ["0","2->4","6","8->9"]
nums = [0,2,3,4,6,8,9]

print(sol.summaryRanges(nums=nums))