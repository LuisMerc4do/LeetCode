class Solution:
    def longestUnivaluePath(self, root):
        self.max_lenght = 0
        def dfs(node):
            if not node:
                return 0 
            left_leght = dfs(node.left)
            right_lenght = dfs(node.right)
            
            left_arrow = right_arrow = 0
            # check if children have the same value as the current node
            # which means we can extend the univalue path by including the
            # current node
            if node.left and node.left.val == node.val:
                left_arrow = left_leght + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_lenght + 1
            
            # left arrow + right arrow is the length of the longest
            # univalue path that goes through the current node
            self.max_lenght = max(max_lenght, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        dfs(root)
        return self.max_lenght
    