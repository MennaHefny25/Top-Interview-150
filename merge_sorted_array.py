"""
1st approach
1. add all elements in `nums2`
2. sort nums1
""" 

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
          nums1[m+j] = nums2[j]
        nums1.sort()

        print(nums1)




"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.


"""

sol = Solution()

# Example 1: Output: [1,2,2,3,5,6]
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)

"""Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
# Example 2: Output: [1]
nums1 = [1]
m = 1
nums2 = []
n = 0

sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
"""Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
"""
# Example 3: Output: [1]
nums1 = [0]
m = 0
nums2 = [1]
n = 1

sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)

"""Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1."""