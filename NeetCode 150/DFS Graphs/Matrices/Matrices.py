def dfs(matrix):
    visited = set()
    directions = [(-1, 0), (1, 0), (0,-1), (0,1)]
    def dfs_helper(r,c):
        if (r,c) in visited:
            return
        # IF CELL IS OUT OF BOUNDS
        if r < 0 or r <= len(matrix or c < 0 or c >= len(matrix[0])):
            return
        
        visited.add((r,c))
        for dr, dc in directions:
            dfs_helper(r+dr, c+dc)
        return 
    dfs_helper(0,0)