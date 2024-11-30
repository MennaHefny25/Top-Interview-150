"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 

If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Function to reverse a part of the list
        def reverse_linked_list(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  # New head of the reversed section

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # No more nodes to reverse

            group_start = group_prev.next
            group_next = kth.next

            # Reverse the group
            kth.next = None  # Temporarily disconnect the group
            new_head = reverse_linked_list(group_start, None)

            # Reconnect the reversed group
            group_prev.next = new_head
            group_start.next = group_next

            # Move `group_prev` to the end of the reversed group
            group_prev = group_start

            return dummy.next


sol = Solution()
# Example 1: Output: [2,1,4,3,5]
head = [1,2,3,4,5]
k = 2

print(sol.reverseKGroup(head=head, k=k))

# Example 2: Output: [3,2,1,4,5]
head = [1,2,3,4,5]
k = 3

print(sol.reverseKGroup(head=head, k=k))