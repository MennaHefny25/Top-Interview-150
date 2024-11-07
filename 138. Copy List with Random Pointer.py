"""
A linked list of length n is given such that each node contains an additional random pointer, 

which could point to any node in the list, or null.

Construct a deep copy of the list. 

The deep copy should consist of exactly n brand new nodes, 

where each new node has its value set to the value of its corresponding original node. 

Both the next and random pointer of the new nodes should point to new nodes in 

the copied list such that the pointers in the original list and copied list represent the same list state. 

None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 

then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 

Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Create new nodes interweaved with the original list
        curr = head
        while curr:
            new_node = Node(curr.val)  # Create a new node with the same value
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Set the random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next  # Set the random pointer for the new node
            curr = curr.next.next  # Move to the next original node

        # Step 3: Separate the original list and the copied list
        curr = head
        copied_head = head.next  # The head of the copied list
        while curr:
            copied_node = curr.next
            curr.next = copied_node.next  # Restore the original list's next pointer
            if copied_node.next:
                copied_node.next = copied_node.next.next  # Set the next pointer of the copied node
            curr = curr.next

        return copied_head


sol = Solution()
# Example 1: Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]

print(sol.copyRandomList(head=head))

# Example 2: Output: [[1,1],[2,1]]
head = [[1,1],[2,1]]

print(sol.copyRandomList(head=head))

# Example 3: Output: [[3,null],[3,0],[3,null]]
head = [[3,None],[3,0],[3,None]]

print(sol.copyRandomList(head=head))