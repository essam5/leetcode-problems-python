class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # I will solve this with Dijkstra but I need to modify on it 
        # first make a heap start with (t, r, c)
        # which mean t is the time or max-height , r is the row 
        # c is the column 

        n = len(grid)
        visit = set()
        # start with (0, 0) with the value of it grid[0][0]
        min_heap = [(grid[0][0], 0, 0)]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if row == n -1 and col == n-1:
                return time

            for r, c in directions:
                nei_r, nei_c = row + r, col + c
                if nei_r < 0 or nei_c < 0 or nei_r >= n or nei_c >= n or (nei_r, nei_c) in visit:
                    continue

                visit.add((nei_r, nei_c))
                heapq.heappush(min_heap, (max(time, grid[nei_r][nei_c]), nei_r, nei_c))




        