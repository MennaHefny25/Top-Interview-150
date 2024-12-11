"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
    
sol = Solution()
# Example 1: Output: [4,7,2,9,6,3,1]
root = [4,2,7,1,3,6,9]

print(sol.invertTree(root=root))

# Example 2: Output: [2,3,1]
root = [2,1,3]

print(sol.invertTree(root=root))

# Example 3: Output: []
root = []

print(sol.invertTree(root=root))