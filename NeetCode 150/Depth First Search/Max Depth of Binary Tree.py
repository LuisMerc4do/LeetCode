# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # Base Case when recursion stops
        if not root:
            return 0
        # Call the left side of the tree
        left = maxDepth(root.left)
        # Call right side of the tree
        right = maxDepth(root.right)
        # Each node return max depth + parent node (1)
        return (left, right) + 1