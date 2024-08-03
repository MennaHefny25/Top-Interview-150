"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 

find two numbers such that they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 

You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

# 1st solution
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr_1, ptr_2 = 0, len(numbers) -1
        temp_sum = 0
        while ptr_1 < ptr_2:
            temp_sum = numbers[ptr_1] + numbers[ptr_2]
            if temp_sum == target: # they add up to a specific target number
                return [ptr_1+1 , ptr_2+1]
            elif temp_sum < target:
                ptr_1 +=1
            else:
                ptr_2 -=1 


sol = Solution()
# Example 1: Output: [1,2]
numbers = [2,7,11,15]
target = 9

print(sol.twoSum(numbers=numbers, target=target))





# Example 2: Output: [1,3]
numbers = [2,3,4]
target = 6

print(sol.twoSum(numbers=numbers, target=target))



# Example 3: Output: [1,2]
numbers = [-1,0]
target = -1

print(sol.twoSum(numbers=numbers, target=target))