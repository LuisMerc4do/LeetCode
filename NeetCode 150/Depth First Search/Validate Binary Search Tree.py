class Solution:
    def validateBST(self, root):
        def dfs(node, min_, max_):
            # base case
            if not node:
                return True
            # check if current node value is within the valid range
            if node.val <= min_ or node.val >= max_:
                return False 
            # so we check left if node is greater that parent
            left = dfs(node.left, min_, node.val)
            # so we check right if node is less than parent
            right = dfs(node.right, node.val, max_)
            return left or right
        return dfs(root, float("inf"), float("inf"))
    