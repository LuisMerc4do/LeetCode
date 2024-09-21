def maxValue(node):
    if node is None:
        return float("-inf")
    if node.left is None and node.right is None:
        return node.val
    left = maxValue(node.left)
    right = maxValue(node.right)
    return max(left, right, node.val)