"""
Given the head of a singly linked list and two integers left and right where left <= right, 

reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        # Step 1: Setup a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Move `prev` to the node before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Reverse the sublist
        current = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp

        # Step 4: Reconnect the reversed sublist with the original list
        prev.next.next = current  # Tail of reversed sublist connects to `current`
        prev.next = next_node  # `prev` connects to the new head of the reversed sublist

        return dummy.next
        



sol = Solution()
# Example 1: Output: [1,4,3,2,5]
head = [1,2,3,4,5]
left = 2
right = 4

print(sol.reverseBetween(head=head, left=left, right=right))

# Example 2: Output: [5]
head = [5]
left = 1
right = 1

print(sol.reverseBetween(head=head, left=left, right=right))

