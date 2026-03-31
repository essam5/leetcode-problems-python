class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions
        # loop for both rows, cols 
        # if == 1 make dfs , the dfs loop on the directions 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if r >= rows or c >=cols or r < 0 or c < 0 or grid[r][c] == "0":
                return 
            grid[r][c] = "0"    
            
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands            