def dfs(node):
    if node is None:
        return 0
    # base case: leaf node
    if node.left is None and node.right is None:
        return node.val
    
    left = dfs(node.left)
    right = dfs(node.right)
    return left + right + node.val