class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        1- get rows, cols and make a set for pac, and atl 
        2- loop throw the cols to get (the rows values)
         the top for pac and bottom for atl
        3- same loop but throw rows to get (right column values for pac)
         (left column values for atl)
        4- the dfs will be (r, c, visit, prev_hieght)
        visit like pac or atl 
        and loop on the all directions   

        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            # visit maybe pac or atl
            if ((r,c) in visit 
                or r <0 or c < 0 
                or r == rows or c == cols
                or heights[r][c] < prev_height):
                # not make any thing 
                return  
            visit.add((r,c))    

            dfs(r+1 ,c    , visit, heights[r][c])
            dfs(r-1 , c   , visit, heights[r][c])
            dfs(r   , c+1 , visit, heights[r][c])
            dfs(r   , c-1 , visit, heights[r][c])    

        # get the top values and bottom values
        for c in range(cols):
            # 0 for first row 
            # height[0][c] that to save the previous value 
            # to compare inside the dfs
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        # adding the result 
        result = []
        for r in range(rows):
            for c in range(cols):
                # must in both pac and atl 
                if (r, c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result                    

        