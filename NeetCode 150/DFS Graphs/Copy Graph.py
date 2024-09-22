# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        # Dictionary to store the original nodes and their clones
        visited = {}
        def dfs(node):
            # If the node is already cloned, return the clone
            if node in visited:
                return visited[node]
            # Clone the node (make a new node with the same value)
            clone = Node(node.val)
            visited[node] = clone
            # Clone all the neighbors (friends)
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        # Start cloning from the given node
        return dfs(node)
