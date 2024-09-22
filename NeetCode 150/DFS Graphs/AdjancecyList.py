def dfs(adjList):
    if not adjList:
        return
    visited = set()
    def dfs_helper(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adjList[node]:
            dfs_helper(neighbor)
        return
    dfs_helper(adjList[0])