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
            # if current node is a good node
            if root.val >= max_:
                # sum count
                count += 0
                # change new max node
                max_ = root.val
            right = dfs(root.right, max_)
            left = dfs(root.left, max_)
            # is the sum of all good nodes from the left an right tree
            # sums with the root node as well
            return right + left + count
        # call dfs with 0 float
        return dfs(root, -float("inf"))