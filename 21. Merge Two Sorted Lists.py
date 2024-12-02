"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode()
        current = merged

        # While both lists have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one of the lists is not traversed, attach the rest of the nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list, which starts at merged.next
        return merged.next
                




sol = Solution()
# Example 1: Output: [1,1,2,3,4,4]
list1 = [1,2,4]
list2 = [1,3,4]

print(sol.mergeTwoLists())

# Example 2: Output: []
list1 = []
list2 = []

print(sol.mergeTwoLists())

# Example 3: Output: [0]
list1 = []
list2 = [0]

print(sol.mergeTwoLists())