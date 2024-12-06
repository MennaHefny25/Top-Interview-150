"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
            
        # Step 1: Calculate the length of the list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Normalize k
        k %= length
        if k == 0:
            return head
        
        # Step 3: Find the new head
        steps_to_new_head = length - k
        current = head
        for _ in range(steps_to_new_head - 1):
            current = current.next
        
        # Step 4: Rearrange pointers
        new_head = current.next
        current.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        return new_head

sol = Solution()
# Example 1: Output: [4,5,1,2,3]
head = [1,2,3,4,5]
k = 2

print(sol.rotateRight(head=head, k=k))

# Example 2: Output: [2,0,1]
head = [0,1,2]
k = 4

print(sol.rotateRight(head=head, k=k))