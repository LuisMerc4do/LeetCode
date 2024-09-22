class Solution:
    def diameterOfBinaryTree(self, root):
        max_ = 0
        def dfs(node):
            nonlocal max_
            #base case
            if not node:
                return 0
            # get the max depth of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # update the maximum diameter of the tree
            max_ = max(max_, left + right)
            
            # return the max depth of the current subtree
            return 1 + max(left, right)
        dfs(root)
        return max_