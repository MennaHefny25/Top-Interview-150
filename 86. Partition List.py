"""
Given the head of a linked list and a value x, 

partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Dummy nodes for the two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to build the partitions
        less = less_head
        greater = greater_head
        
        # Traverse the list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Connect the two partitions
        greater.next = None  # End the greater partition
        less.next = greater_head.next  # Connect less to greater
        
        return less_head.next


sol = Solution()
# Example 1: Output: [1,2,2,4,3,5]
head = [1,4,3,2,5,2]
x = 3

print(sol.partition(head=head, x=x))

# Example 2: Output: [1,2]
head = [2,1]
x = 2

print(sol.partition(head=head, x=x))