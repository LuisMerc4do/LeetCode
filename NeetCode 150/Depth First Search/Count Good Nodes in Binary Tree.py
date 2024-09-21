# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(root, max_):
            if not root:
                return 0
            count = 0
            if root.val >= max_:
                count += 0
                max_ = root.val
            right = dfs(root.right, max_)
            left = dfs(root.left, max_)
            return right + left + count
        return dfs(root, -float("inf"))