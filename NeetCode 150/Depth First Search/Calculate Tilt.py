class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root):
            if not node:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.count += abs(left - right)
            return left + right + root.val
        dfs(root)
        return self.count