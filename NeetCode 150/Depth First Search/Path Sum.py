class Solution:
    def pathSum(self, root, target):
        # BASE CASE
        if not root:
            return None
        # WHAT IF THERE IS A LEAF NODE
        # We cant go further so we check the sum, is already - all the other nodes
        if not root.right and not root.left:
            # Leaf node is the same as the value we are looking for ?
            return root.val == target
        # We apply recursion and we - the value of the node to the target
        left = self.pathSum(root.left, target - root.val)
        right = self.pathSum(root.right, target - root.val)
        
        # If any path found return
        return left or right