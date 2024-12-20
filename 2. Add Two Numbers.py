"""
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ListNode_obj = ListNode()
        current = ListNode_obj
        carry = 0

        while l1 or l2 or carry:
            # Get values to be summed
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            # Calculate sum
            total = val_1 + val_2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Advance to the next node
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ListNode_obj.next


sol = Solution()
# Example 1: Output: [7,0,8]
l1 = [2,4,3]
l2 = [5,6,4]

print(sol.addTwoNumbers(l1=l1, l2=l2))

# Example 2: Output: [0]
l1 = [0]
l2 = [0]

print(sol.addTwoNumbers(l1=l1, l2=l2))

# Example 3: Output: [8,9,9,9,0,0,0,1]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(sol.addTwoNumbers(l1=l1, l2=l2))