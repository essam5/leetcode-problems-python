class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first count the fresh orange
        # adding the rotten orange to queue to loop on it simultaneously

        # loop till we have a rotten in queue and we have fresh orange
        # loop in the range of len queue as a level of all rotten orange
        # make the check for round out or make it rot and -1 fresh

        fresh_count = 0
        time = 0
        queue = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count +=1
                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        while queue and fresh_count >0:
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row+dr, col + dc

                    if r<0 or c<0 or r>= rows or c>= cols or grid[r][c] != 1:
                        continue

                    grid[r][c] = 2
                    queue.append((r,c))  
                    fresh_count -= 1

            time +=1    

        return time if fresh_count == 0 else -1              





        