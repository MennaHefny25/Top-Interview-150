"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 

leaving only distinct numbers from the original list. 

Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # Tracks the last node before the duplicate sequence

        while head:
            # Detect duplicate values
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Remove duplicates
                prev.next = head.next
            else:
                # No duplicates, move `prev` forward
                prev = prev.next
            # Move `head` forward
            head = head.next

        return dummy.next

sol = Solution()
# Example 1: Output: [1,2,5]
head = [1,2,3,3,4,4,5]

print(sol.deleteDuplicates(head=head))

# Example 2: Output: [2,3]
head = [1,1,1,2,3]

print(sol.deleteDuplicates(head=head))