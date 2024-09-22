class Solution:
    def pathSum(self, root, target):
        def dfs(node, target, path):
            # base case
            if not node:
                return
            # append current value to the path
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    result.append(path[:])
            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)
            # when our code reaches here, are done exploring all
            # the root-to-leaf paths that go through the current node.
            # pop the current value from the path to prepare for the next path
            path.pop()
        result = []
        dfs(root, target, [])
        return result