"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize left and right pointers
        left = right = dummy
        
        # Move the right pointer n + 1 steps ahead
        for _ in range(n + 1):
            right = right.next
        
        # Move both pointers until the right pointer reaches the end
        while right:
            right = right.next
            left = left.next
        
        # Remove the nth node
        left.next = left.next.next
                
        return dummy.next
        


sol = Solution()
# Example 1: Output: [1,2,3,5]
head = [1,2,3,4,5]
n = 2

print(sol.removeNthFromEnd(head=head, n=n))

# Example 2: Output: []
head = [1]
n = 1

print(sol.removeNthFromEnd(head=head, n=n))

# Example 3: Output: [1]
head = [1,2]
n = 1

print(sol.removeNthFromEnd(head=head, n=n))