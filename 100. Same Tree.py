"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


sol = Solution()
# Example 1: Output: true
p = [1,2,3]
q = [1,2,3]

print(sol.isSameTree(p=p, q=q))

# Example 2: Output: false
p = [1,2]
q = [1,None,2]

print(sol.isSameTree(p=p, q=q))

# Example 3: Output: false
p = [1,2,1]
q = [1,1,2]

print(sol.isSameTree(p=p, q=q))